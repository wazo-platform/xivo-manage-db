"""Add default template webrtc_video

Revision ID: ea9cdf2d59f8
Revises: bf1aaa27b7f8

"""

import string
import random

from alembic import op
import sqlalchemy as sa
from sqlalchemy import sql

from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = "ea9cdf2d59f8"
down_revision = "bf1aaa27b7f8"

ALPHANUMERIC_POOL = string.ascii_lowercase + string.digits
WEBRTC_VIDEO_COLUMN_NAME = "webrtc_video_sip_template_uuid"

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
    sa.sql.column("webrtc_sip_template_uuid"),
    sa.sql.column(WEBRTC_VIDEO_COLUMN_NAME),
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


def insert_webrtc_video_endpoint(tenant_uuid, webrtc_sip_template_uuid):
    query = (
        endpoint_sip_tbl.insert()
        .returning(endpoint_sip_tbl.c.uuid)
        .values(
            label='webrtc_video',
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
            type='endpoint',
        )
    )
    endpoint_section_uuid = op.get_bind().execute(query).scalar()

    options = [
        ("max_video_streams", "25"),
        ("max_audio_streams", "1"),
    ]
    for key, value in options:
        query = (
            endpoint_sip_section_option_tbl
            .insert()
            .values(
                key=key,
                value=value,
                endpoint_sip_section_uuid=endpoint_section_uuid,
            )
        )
        op.execute(query)

    query = (
        endpoint_sip_template_tbl
        .insert()
        .values(
            child_uuid=endpoint_sip_uuid,
            parent_uuid=webrtc_sip_template_uuid,
        )
    )
    op.execute(query)

    return endpoint_sip_uuid


def configure_tenant(tenant_uuid, webrtc_sip_template_uuid):
    # 1. Create default template and assign to tenant
    webrtc_video_uuid = insert_webrtc_video_endpoint(
        tenant_uuid,
        webrtc_sip_template_uuid
    )

    op.execute(
        tenant_tbl.update()
        .values(
            webrtc_video_sip_template_uuid=webrtc_video_uuid,
        )
        .where(tenant_tbl.c.uuid == tenant_uuid)
    )

    # 2. Find sip endpoint with matching params
    query = (
        sa.sql.select([endpoint_sip_tbl.c.uuid])
        .select_from(
            endpoint_sip_tbl
            .join(
                endpoint_sip_section_tbl,
                endpoint_sip_section_tbl.c.endpoint_sip_uuid == endpoint_sip_tbl.c.uuid,
            )
            .join(
                endpoint_sip_section_option_tbl,
                endpoint_sip_section_option_tbl.c.endpoint_sip_section_uuid == endpoint_sip_section_tbl.c.uuid,
            )
        )
        .where(endpoint_sip_tbl.c.template.is_(False))
        .where(endpoint_sip_tbl.c.tenant_uuid == tenant_uuid)
        .where(endpoint_sip_section_tbl.c.type == 'endpoint')
        .where(
            sql.or_(
                sql.and_(
                    endpoint_sip_section_option_tbl.c.key == 'max_video_streams',
                    endpoint_sip_section_option_tbl.c.value == '25',
                ),
                sql.and_(
                    endpoint_sip_section_option_tbl.c.key == 'max_audio_streams',
                    endpoint_sip_section_option_tbl.c.value == '1',
                ),
            )
        )
        .group_by(endpoint_sip_tbl.c.uuid)
    )
    endpoints = op.get_bind().execute(query)

    for endpoint in endpoints:
        query = (
            endpoint_sip_template_tbl
            .insert()
            .values(
                child_uuid=endpoint.uuid,
                parent_uuid=webrtc_video_uuid,
            )
        )
        op.execute(query)


def upgrade():
    # 1. Add new column to tenant table
    op.add_column(
        "tenant",
        sa.Column(
            WEBRTC_VIDEO_COLUMN_NAME,
            UUID,
            sa.ForeignKey(
                "endpoint_sip.uuid",
                ondelete="SET NULL",
                name="tenant_webrtc_video_sip_template_uuid_fkey",
            ),
        ),
    )

    # 2. Assign template to tenants
    query = sa.sql.select([tenant_tbl.c.uuid, tenant_tbl.c.webrtc_sip_template_uuid])
    tenants = op.get_bind().execute(query)
    for tenant in tenants:
        configure_tenant(tenant.uuid, tenant.webrtc_sip_template_uuid)

    # 3. Delete options matching default params
    query = (
        endpoint_sip_section_option_tbl
        .delete()
        .where(
            sql.or_(
                sql.and_(
                    endpoint_sip_section_option_tbl.c.key == 'max_video_streams',
                    endpoint_sip_section_option_tbl.c.value == '25',
                ),
                sql.and_(
                    endpoint_sip_section_option_tbl.c.key == 'max_audio_streams',
                    endpoint_sip_section_option_tbl.c.value == '1',
                ),
            )
        )
    )
    op.execute(query)


def downgrade():
    # 1. Drop templates webrtc_video
    query = (
        endpoint_sip_tbl
        .delete()
        .where(endpoint_sip_tbl.c.uuid.in_(
            sql.select([tenant_tbl.c.webrtc_video_sip_template_uuid])
        ))
    )
    op.get_bind().execute(query)

    # 2. Drop table column
    op.drop_column("tenant", WEBRTC_VIDEO_COLUMN_NAME)
