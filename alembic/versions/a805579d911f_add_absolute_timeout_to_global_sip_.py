"""add absolute timeout to global sip templates

Revision ID: a805579d911f
Revises: 65b4ba443641

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a805579d911f'
down_revision = '65b4ba443641'

endpoint_sip_table = sa.sql.table(
    "endpoint_sip",
    sa.sql.column("uuid"),
    sa.sql.column("template"),
    sa.sql.column("label"),
)
endpoint_sip_section_table = sa.sql.table(
    "endpoint_sip_section",
    sa.sql.column("endpoint_sip_uuid"),
    sa.sql.column("uuid"),
)
endpoint_sip_section_option_table = sa.sql.table(
    "endpoint_sip_section_option",
    sa.sql.column("endpoint_sip_section_uuid"),
    sa.sql.column("uuid"),
)
tenant_table = sa.sql.table(
    "tenant",
    sa.sql.column("uuid"),
    sa.sql.column("global_sip_template_uuid")
)



def find_tenants():
    query = sa.sql.select([
        tenant_table.c.uuid,
        tenant_table.c.global_sip_template_uuid
    ])
    return query


def get_sip_endpoint_global_templates():
    """
    select endpoint_sip.tenant_uuid, endpoint_sip.label, esc.endpoint_sip_uuid, 
    esc.type as section_type, esco.key, esco.value as endpoint_uuid 
    from endpoint_sip_section_option as esco 
    left join endpoint_sip_section as esc on esc.uuid = esco.endpoint_sip_section_uuid 
    left join endpoint_sip on esc.endpoint_sip_uuid = endpoint_sip.uuid 
    where endpoint_sip.template and endpoint_sip.label = 'global';
    """
    query = sa.sql.select([
        tenant_table.c.global_sip_template_uuid
    ]).select_from(
        endpoint_sip_table
    )
    return query


def get_global_sip_template_with_set_var_options():
    query = sa.sql.select([
        endpoint_sip_table.c.uuid,
        endpoint_sip_table.c.tenant_uuid,
        endpoint_sip_section_option_table.c.key,
        endpoint_sip_section_option_table.c.value
    ]).select_from(
        endpoint_sip_section_option_table
    ).join(
        endpoint_sip_section_table,
        endpoint_sip_section_table.c.uuid == endpoint_sip_section_option_table.c.endpoint_sip_section_uuid
    ).join(
        endpoint_sip_table,
        endpoint_sip_table.c.uuid == endpoint_sip_section_table.c.endpoint_sip_uuid
    ).where(
        sa.sql.and_(
            endpoint_sip_table.c.template,
            endpoint_sip_table.c.uuid.in_(get_sip_endpoint_global_templates()),
            endpoint_sip_section_table.c.type == 'endpoint',
            endpoint_sip_section_option_table.c.key == 'set_var',
        )
    )
    return query


def upgrade():
    sip_templates_with_timeout_set_var = {
        row.uuid
        for row in get_global_sip_template_with_set_var_options()
        if row.value.startswith('TIMEOUT(absolute)')
    }
    global_sip_templates = get_sip_endpoint_global_templates()

    new_options = sa.sql.insert(endpoint_sip_section_option_table).values(
        endpoint_sip_section_uuid=sa.sql.bindparam('endpoint_sip_uuid'),
        key='set_var',
        value='TIMEOUT(absolute)=36000'
    )
    global_sip_template_endpoint_sections = sa.sql.select([
        endpoint_sip_section_table.c.uuid
    ]).where(
        sa.sql.and_(
            endpoint_sip_section_table.c.endpoint_sip_uuid.in_(global_sip_templates),
            endpoint_sip_section_table.c.type == 'endpoint',
        )
    )

    op.get_bind().execute(
        new_options,
        [
            {
                'endpoint_sip_uuid': row.uuid
            }
            for row in global_sip_template_endpoint_sections
            if row.uuid not in sip_templates_with_timeout_set_var
        ]
    )



def downgrade():
    pass
