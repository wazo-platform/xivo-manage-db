"""add-togglerecord-to-global-template

Revision ID: 58b1be9f53cd
Revises: 43f7a8ecb70c

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = '58b1be9f53cd'
down_revision = '43f7a8ecb70c'

endpoint_sip_section_option_table = sa.sql.table(
    "endpoint_sip_section_option",
    sa.sql.column("endpoint_sip_section_uuid"),
    sa.sql.column("uuid"),
    sa.sql.column("key"),
    sa.sql.column("value"),
)
endpoint_sip_section_table = sa.sql.table(
    "endpoint_sip_section",
    sa.sql.column("endpoint_sip_uuid"),
    sa.sql.column("uuid"),
    sa.sql.column("type"),
)
endpoint_sip_table = sa.sql.table(
    "endpoint_sip",
    sa.sql.column("uuid"),
    sa.sql.column("template"),
    sa.sql.column("label"),
    sa.sql.column("tenant_uuid"),
)
tenant_table = sa.sql.table(
    "tenant",
    sa.sql.column("uuid"),
    sa.sql.column("global_sip_template_uuid")
)

def get_sip_endpoint_global_templates() -> sa.sql.Selectable:
    query = sa.sql.select([
        endpoint_sip_table.c.uuid,
    ]).select_from(
        endpoint_sip_table.join(
            tenant_table,
            tenant_table.c.global_sip_template_uuid == endpoint_sip_table.c.uuid
        )
    )
    return query


def get_global_sip_template_with_togglerecord_configured():
    target = endpoint_sip_section_option_table.join(
        endpoint_sip_section_table,
        endpoint_sip_section_table.c.uuid == 
        endpoint_sip_section_option_table.c.endpoint_sip_section_uuid
    ).join(
        endpoint_sip_table,
        endpoint_sip_table.c.uuid == endpoint_sip_section_table.c.endpoint_sip_uuid
    )

    # get endpoint uuid for templates with 'set_var' options in 'endpoint' sections
    query = sa.sql.select([
        sa.sql.distinct(endpoint_sip_table.c.uuid)
    ]).select_from(
        target
    ).where(
        sa.sql.and_(
            endpoint_sip_table.c.template,
            endpoint_sip_table.c.uuid.in_(get_sip_endpoint_global_templates()),
            endpoint_sip_section_table.c.type == 'endpoint',
            endpoint_sip_section_option_table.c.key == 'set_var',
            endpoint_sip_section_option_table.c.value == ('DYNAMIC_FEATURES=togglerecord'),
        )
    )
    return query

def upgrade():
    new_options = sa.sql.insert(endpoint_sip_section_option_table).from_select(
        [
            'key',
            'value',
            'endpoint_sip_section_uuid'
        ],
        sa.sql.select([
            sa.sql.literal('set_var'),
            sa.sql.literal('DYNAMIC_FEATURES=togglerecord'),
            endpoint_sip_section_table.c.uuid
        ]).where(
            sa.sql.and_(
                endpoint_sip_section_table.c.endpoint_sip_uuid.in_(
                    get_sip_endpoint_global_templates().where(
                        endpoint_sip_table.c.uuid.notin_(
                            get_global_sip_template_with_togglerecord_configured()
                        )
                )),
                endpoint_sip_section_table.c.type == 'endpoint',
            )
        )
    )

    _ = op.get_bind().execute(
        new_options
    )


def downgrade():
    pass
