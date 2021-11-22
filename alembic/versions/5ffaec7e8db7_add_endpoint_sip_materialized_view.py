"""add endpoint_sip materialized view

Revision ID: 5ffaec7e8db7
Revises: 61e3d7c65755

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB, aggregate_order_by
from sqlalchemy.ext import compiler
from sqlalchemy.schema import DDLElement
from sqlalchemy.sql.functions import array_agg, func


# revision identifiers, used by Alembic.
revision = '5ffaec7e8db7'
down_revision = '61e3d7c65755'


class CreateMaterializedView(DDLElement):
    def __init__(self, name, selectable):
        self.name = name
        self.selectable = selectable


@compiler.compiles(CreateMaterializedView)
def _compile_create_view(element, compiler, **kw):
    name = compiler.dialect.identifier_preparer.quote(element.name)
    selectable = compiler.sql_compiler.process(element.selectable, literal_binds=True)
    return 'CREATE MATERIALIZED VIEW {} AS {}'.format(name, selectable)


# TODO: Replace by SQLAlchemy-Utils when possible
class DropMaterializedView(DDLElement):
    def __init__(self, name, cascade=True):
        self.name = name
        self.cascade = cascade


@compiler.compiles(DropMaterializedView)
def _compile_drop_view(element, compiler, **kw):
    name = compiler.dialect.identifier_preparer.quote(element.name)
    cascade = 'CASCADE ' if element.cascade else ''
    return 'DROP MATERIALIZED VIEW IF EXISTS {} {}'.format(name, cascade)


def generate_view_selectable():
    cte = (
        sa.select(
            [
                sa.literal_column('endpoint_sip.uuid').label('uuid'),
                sa.literal(0).label('level'),
                sa.literal('0', sa.String).label('path'),
                sa.literal_column('endpoint_sip.uuid').label('root'),
            ]
        )
        .select_from(sa.table('endpoint_sip'))
        .cte(recursive=True)
    )

    endpoints = cte.union_all(
        sa.select(
            [
                sa.literal_column('endpoint_sip_template.parent_uuid').label('uuid'),
                (cte.c.level + 1).label('level'),
                (
                    cte.c.path
                    + sa.cast(
                        func.row_number().over(
                            partition_by='level',
                            order_by=sa.literal_column(
                                'endpoint_sip_template.priority'
                            ),
                        ),
                        sa.String,
                    )
                ).label('path'),
                (cte.c.root),
            ]
        ).select_from(
            sa.join(
                cte,
                sa.table('endpoint_sip_template'),
                cte.c.uuid == sa.literal_column('endpoint_sip_template.child_uuid'),
            )
        )
    )

    return (
        sa.select(
            [
                endpoints.c.root,
                sa.cast(
                    sa.func.jsonb_object(
                        array_agg(
                            aggregate_order_by(
                                sa.literal_column('endpoint_sip_section_option.key'),
                                endpoints.c.path.desc(),
                            )
                        ),
                        array_agg(
                            aggregate_order_by(
                                sa.literal_column('endpoint_sip_section_option.value'),
                                endpoints.c.path.desc(),
                            )
                        ),
                    ),
                    JSONB,
                ).label('options'),
            ]
        )
        .select_from(
            sa.join(
                endpoints,
                sa.table('endpoint_sip_section'),
                sa.literal_column('endpoint_sip_section.endpoint_sip_uuid')
                == endpoints.c.uuid,
            ).join(
                sa.table('endpoint_sip_section_option'),
                sa.literal_column(
                    'endpoint_sip_section_option.endpoint_sip_section_uuid'
                )
                == sa.literal_column('endpoint_sip_section.uuid'),
            )
        )
        .group_by(endpoints.c.root)
    )


def upgrade():
    op.execute(
        CreateMaterializedView('endpoint_sip_options_view', generate_view_selectable())
    )
    op.create_index(
        'endpoint_sip_options_view__idx_root',
        'endpoint_sip_options_view',
        ['root'],
        unique=True,
    )


def downgrade():
    op.drop_index('endpoint_sip_options_view__idx_root', 'endpoint_sip_mv')
    op.execute(DropMaterializedView('endpoint_sip_options_view'))
