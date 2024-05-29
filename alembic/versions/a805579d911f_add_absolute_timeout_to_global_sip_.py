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
    sa.sql.column("tenant_uuid"),
)
endpoint_sip_section_table = sa.sql.table(
    "endpoint_sip_section",
    sa.sql.column("endpoint_sip_uuid"),
    sa.sql.column("uuid"),
    sa.sql.column("type"),
)
endpoint_sip_section_option_table = sa.sql.table(
    "endpoint_sip_section_option",
    sa.sql.column("endpoint_sip_section_uuid"),
    sa.sql.column("uuid"),
    sa.sql.column("key"),
    sa.sql.column("value"),
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


def get_global_sip_template_with_timeout_configured():
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
            endpoint_sip_section_option_table.c.value.startswith('TIMEOUT(absolute)='),
        )
    )
    return query


def upgrade() -> None:
    new_options = sa.sql.insert(endpoint_sip_section_option_table).from_select(
        [
            'key',
            'value',
            'endpoint_sip_section_uuid'
        ],
        sa.sql.select([
            sa.sql.literal('set_var'),
            sa.sql.literal('TIMEOUT(absolute)=36000'),
            endpoint_sip_section_table.c.uuid
        ]).where(
            sa.sql.and_(
                endpoint_sip_section_table.c.endpoint_sip_uuid.in_(
                    get_sip_endpoint_global_templates().where(
                        endpoint_sip_table.c.uuid.notin_(
                            get_global_sip_template_with_timeout_configured()
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
    # delete sip global templates 'set_var' endpoint options with value `TIMEOUT(absolute)=36000`
    sip_template_options = sa.sql.select([endpoint_sip_section_option_table.c.uuid]).select_from(
        endpoint_sip_section_option_table.join(
        endpoint_sip_section_table,
        endpoint_sip_section_table.c.uuid == endpoint_sip_section_option_table.c.endpoint_sip_section_uuid
    )).where(
        sa.sql.and_(
            endpoint_sip_section_table.c.type == 'endpoint',
            endpoint_sip_section_option_table.c.key == 'set_var',
            endpoint_sip_section_option_table.c.value == 'TIMEOUT(absolute)=36000',
            endpoint_sip_section_table.c.endpoint_sip_uuid.in_(
                get_sip_endpoint_global_templates()
            )
        )
    )
    remove_timeout_options = sa.sql.delete(endpoint_sip_section_option_table).where(
        endpoint_sip_section_option_table.c.uuid.in_(
            sip_template_options
        )
    )
    _ = op.get_bind().execute(
        remove_timeout_options
    )
