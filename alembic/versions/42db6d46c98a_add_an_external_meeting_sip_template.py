"""add an external meeting sip template

Revision ID: 42db6d46c98a
Revises: 706a7655606e

"""

import string
import random

from alembic import op
import sqlalchemy as sa
from sqlalchemy import sql

from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = "42db6d46c98a"
down_revision = "706a7655606e"

ALPHANUMERIC_POOL = string.ascii_lowercase + string.digits
MEETING_GUEST_COLUMN_NAME = "meeting_guest_sip_template_uuid"

transport_option_tbl = sa.sql.table(
    "pjsip_transport_option",
    sa.sql.column("key"),
    sa.sql.column("value"),
)
endpoint_sip_tbl = sa.sql.table(
    "endpoint_sip",
    sa.sql.column("uuid"),
    sa.sql.column("label"),
    sa.sql.column("name"),
    sa.sql.column("tenant_uuid"),
    sa.sql.column("template"),
)
endpoint_sip_section_tbl = sa.sql.table(
    "endpoint_sip_section",
    sa.sql.column("uuid"),
    sa.sql.column("type"),
    sa.sql.column("endpoint_sip_uuid"),
)
endpoint_sip_section_option_tbl = sa.sql.table(
    "endpoint_sip_section_option",
    sa.sql.column("uuid"),
    sa.sql.column("key"),
    sa.sql.column("value"),
    sa.sql.column("endpoint_sip_section_uuid"),
)
endpoint_sip_template_tbl = sa.sql.table(
    "endpoint_sip_template",
    sa.sql.column("child_uuid"),
    sa.sql.column("parent_uuid"),
)
tenant_tbl = sa.sql.table(
    "tenant",
    sa.sql.column("uuid"),
    sa.sql.column("webrtc_video_sip_template_uuid"),
    sa.sql.column(MEETING_GUEST_COLUMN_NAME),
)


def name_already_exists(name):
    query = sa.sql.select([endpoint_sip_tbl.c.name]).where(
        endpoint_sip_tbl.c.name == name
    )
    return op.get_bind().execute(query).scalar() is not None


def generate_unused_name():
    while True:
        data = "".join(random.choice(ALPHANUMERIC_POOL) for _ in range(8))
        if not name_already_exists(data):
            return data


def insert_meeting_guest_endpoint(tenant_uuid, webrtc_video_sip_template_uuid):
    query = (
        endpoint_sip_tbl.insert()
        .returning(endpoint_sip_tbl.c.uuid)
        .values(
            label='meeting_guest',
            name=generate_unused_name(),
            tenant_uuid=tenant_uuid,
            template=True,
        )
    )
    endpoint_sip_uuid = op.get_bind().execute(query).scalar()

    query = (
        endpoint_sip_section_tbl.insert()
        .returning(endpoint_sip_section_tbl.c.uuid)
        .values(
            endpoint_sip_uuid=endpoint_sip_uuid,
            type='aor',
        )
    )
    aor_section_uuid = op.get_bind().execute(query).scalar()

    options = [
        ("max_contacts", "50"),
    ]
    for key, value in options:
        query = (
            endpoint_sip_section_option_tbl
            .insert()
            .values(
                key=key,
                value=value,
                endpoint_sip_section_uuid=aor_section_uuid,
            )
        )
        op.execute(query)

    if webrtc_video_sip_template_uuid:
        query = (
            endpoint_sip_template_tbl
            .insert()
            .values(
                child_uuid=endpoint_sip_uuid,
                parent_uuid=webrtc_video_sip_template_uuid,
            )
        )
        op.execute(query)

    return endpoint_sip_uuid


def configure_tenant(tenant_uuid, webrtc_video_sip_template_uuid):
    guest_meeting_uuid = insert_meeting_guest_endpoint(
        tenant_uuid,
        webrtc_video_sip_template_uuid
    )

    op.execute(
        tenant_tbl.update()
        .values(
            meeting_guest_sip_template_uuid=guest_meeting_uuid,
        )
        .where(tenant_tbl.c.uuid == tenant_uuid)
    )


def upgrade():
    # 1. Add new column to tenant table
    op.add_column(
        "tenant",
        sa.Column(
            MEETING_GUEST_COLUMN_NAME,
            UUID,
            sa.ForeignKey(
                "endpoint_sip.uuid",
                ondelete="SET NULL",
                name="tenant_meeting_guest_sip_template_uuid_fkey",
            ),
        ),
    )

    # 2. Assign template to tenants
    query = sa.sql.select([tenant_tbl.c.uuid, tenant_tbl.c.webrtc_video_sip_template_uuid])
    tenants = op.get_bind().execute(query)
    for tenant in tenants:
        configure_tenant(tenant.uuid, tenant.webrtc_video_sip_template_uuid)


def downgrade():
    # 1. Drop templates meeting_guest
    query = (
        endpoint_sip_tbl
        .delete()
        .where(endpoint_sip_tbl.c.uuid.in_(
            sql.select([tenant_tbl.c.meeting_guest_sip_template_uuid])
        ))
    )
    op.get_bind().execute(query)

    # 2. Drop table column
    op.drop_column("tenant", MEETING_GUEST_COLUMN_NAME)
