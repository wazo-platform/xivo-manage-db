"""reorder endpoint sip template

Revision ID: 040b69fd8297
Revises: 2485d7c1f8e9

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '040b69fd8297'
down_revision = '2485d7c1f8e9'

endpoint_sip_template_table = sa.sql.table(
    "endpoint_sip_template",
    sa.sql.column("child_uuid"),
    sa.sql.column("parent_uuid"),
    sa.sql.column("priority"),
)
tenant_table = sa.sql.table(
    "tenant",
    sa.sql.column("uuid"),
    sa.sql.column("global_sip_template_uuid"),
    sa.sql.column("registration_trunk_sip_template_uuid"),
    sa.sql.column("webrtc_sip_template_uuid"),
    sa.sql.column("webrtc_video_sip_template_uuid"),
)


def upgrade():
    reset_endpoint_sip_template_priority()
    for tenant in find_tenants():
        update_endpoint_sip_template_priority(tenant)


def find_tenants():
    query = sa.sql.select([
        tenant_table.c.uuid,
        tenant_table.c.global_sip_template_uuid,
        tenant_table.c.webrtc_sip_template_uuid,
        tenant_table.c.webrtc_video_sip_template_uuid,
        tenant_table.c.registration_trunk_sip_template_uuid,
    ])
    return op.get_bind().execute(query)


def reset_endpoint_sip_template_priority():
    query = (
        endpoint_sip_template_table.update()
        .values(priority=endpoint_sip_template_table.c.priority + 4)
    )
    op.execute(query)


def update_endpoint_sip_template_priority(tenant):
    global_template_uuid = tenant['global_sip_template_uuid']
    webrtc_template_uuid = tenant['webrtc_sip_template_uuid']
    webrtc_video_template_uuid = tenant['webrtc_video_sip_template_uuid']
    registration_trunk_template_uuid = tenant['registration_trunk_sip_template_uuid']

    query = (
        endpoint_sip_template_table.update()
        .values(priority=0)
        .where(endpoint_sip_template_table.c.parent_uuid == global_template_uuid)
    )
    op.execute(query)

    query = (
        endpoint_sip_template_table.update()
        .values(priority=1)
        .where(endpoint_sip_template_table.c.parent_uuid == webrtc_template_uuid)
    )
    op.execute(query)

    query = (
        endpoint_sip_template_table.update()
        .values(priority=2)
        .where(endpoint_sip_template_table.c.parent_uuid == webrtc_video_template_uuid)
    )
    op.execute(query)

    query = (
        endpoint_sip_template_table.update()
        .values(priority=3)
        .where(endpoint_sip_template_table.c.parent_uuid == registration_trunk_template_uuid)
    )
    op.execute(query)


def downgrade():
    pass
