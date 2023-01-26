"""add notify_early_inuse_ringing option to global sip endoint templates

Revision ID: 1264fdcb3e71
Revises: 0269f5e35792

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1264fdcb3e71'
down_revision = '0269f5e35792'

tenant_tbl = sa.sql.table(
    'tenant',
    sa.sql.column('uuid'),
    sa.sql.column('global_sip_template_uuid'),
)

endpoint_sip_tbl = sa.sql.table(
    'endpoint_sip',
    sa.sql.column('uuid'),
    sa.sql.column('template'),
)

endpoint_sip_section_tbl = sa.sql.table(
    'endpoint_sip_section',
    sa.sql.column('uuid'),
    sa.sql.column('type'),
    sa.sql.column('endpoint_sip_uuid'),
)
endpoint_sip_section_option_tbl = sa.sql.table(
    'endpoint_sip_section_option',
    sa.sql.column('key'),
    sa.sql.column('value'),
    sa.sql.column('endpoint_sip_section_uuid'),
)


def find_sip_endoint_template_sections():
    query = sa.sql.select([endpoint_sip_section_tbl.c.uuid]).where(
        sa.and_(
            endpoint_sip_tbl.c.template.is_(True),
            endpoint_sip_section_tbl.c.endpoint_sip_uuid == endpoint_sip_tbl.c.uuid,
            endpoint_sip_section_tbl.c.type == 'endpoint',
        )
    )
    return op.get_bind().execute(query)


def add_notify_early_inuse_ringing_option(sip_endpoint_sections):
    for sip_endpoint_section in sip_endpoint_sections:
        query = (
            endpoint_sip_section_option_tbl
            .insert()
            .values(
                key='notify_early_inuse_ringing',
                value='yes',
                endpoint_sip_section_uuid=sip_endpoint_section.uuid,
            )
        )
        op.execute(query)


def upgrade():
    sip_endpoint_template_sections = find_sip_endoint_template_sections()
    add_notify_early_inuse_ringing_option(sip_endpoint_template_sections)


def downgrade():
    pass
