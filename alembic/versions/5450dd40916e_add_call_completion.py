"""add call completion

Revision ID: 5450dd40916e
Revises: 30f88b362201
XiVO Version: 14.14

"""

# revision identifiers, used by Alembic.
revision = '5450dd40916e'
down_revision = '30f88b362201'

from alembic import op
import sqlalchemy as sa


call_completion_table = sa.sql.table(
    'call_completion',
)

extensions_table = sa.sql.table(
    'extensions',
    sa.sql.column('commented'),
    sa.sql.column('context'),
    sa.sql.column('exten'),
    sa.sql.column('type'),
    sa.sql.column('typeval'),
)


def upgrade():
    _create_cc_table()
    _insert_cc_extensions()


def _create_cc_table():
    op.create_table(
        'call_completion',
        sa.Column('id', sa.Integer),
        sa.Column('enabled', sa.Boolean, nullable=False, server_default='FALSE'),
        sa.Column('cc_offer_timer', sa.Integer, nullable=False, server_default='30'),
        sa.Column('ccbs_available_timer', sa.Integer, nullable=False, server_default='900'),
        sa.Column('ccnr_available_timer', sa.Integer, nullable=False, server_default='900'),
        sa.Column('cc_recall_timer', sa.Integer, nullable=False, server_default='30'),
        sa.PrimaryKeyConstraint('id'),
    )
    op.execute(call_completion_table.insert().values())


def _insert_cc_extensions():
    op.bulk_insert(extensions_table,
        [
            _new_exten_dict('*40', 'ccrequest'),
            _new_exten_dict('*41', 'cccancel'),
        ]
    )


def _new_exten_dict(exten, typeval):
    return {
        'commented': 1,
        'context': 'xivo-features',
        'exten': exten,
        'type': 'extenfeatures',
        'typeval': typeval,
    }


def downgrade():
    _drop_cc_table()
    _delete_cc_extensions()


def _drop_cc_table():
    op.drop_table('call_completion')


def _delete_cc_extensions():
    op.execute(extensions_table
            .delete()
            .where(sa.sql.and_(
                extensions_table.c.type == 'extenfeatures',
                extensions_table.c.typeval.in_(['ccrequest', 'cccancel']))
            ))
