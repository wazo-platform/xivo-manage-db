"""merge sip templates for webrtc

Revision ID: e04b80f8b6fc
Revises: 495accfabe9f

"""

import string
import random
import sqlalchemy as sa

from alembic import op
from sqlalchemy import sql
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = 'e04b80f8b6fc'
down_revision = '495accfabe9f'

ALPHANUMERIC_POOL = string.ascii_lowercase + string.digits
WEBRTC_VIDEO_COLUMN_NAME = "webrtc_video_sip_template_uuid"

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


def reset_or_add_options_to_webrtc_template():
    options = [
        ("max_video_streams", "25"),
        ("max_audio_streams", "1"),
    ]
    for key, value in options:
        endpoint_sip_options_delete_subquery = (
            sql.select([
                endpoint_sip_section_option_tbl.c.uuid
            ])
            .select_from(
                tenant_tbl
                .join(
                    endpoint_sip_section_tbl,
                    endpoint_sip_section_tbl.c.endpoint_sip_uuid == tenant_tbl.c.webrtc_sip_template_uuid,
                )
                .join(
                    endpoint_sip_section_option_tbl,
                    endpoint_sip_section_option_tbl.c.endpoint_sip_section_uuid == endpoint_sip_section_tbl.c.uuid,
                )
            )
            .where(endpoint_sip_section_tbl.c.type == 'endpoint')
            .where(endpoint_sip_section_option_tbl.c.key == key)
        )
        query = (
            endpoint_sip_section_option_tbl
            .delete()
            .where(endpoint_sip_section_option_tbl.c.uuid.in_(endpoint_sip_options_delete_subquery))
        )
        op.execute(query)
        endpoint_sip_options_insert_subquery = (
            sql.select([
                endpoint_sip_section_tbl.c.uuid,
                sql.literal(key),
                sql.literal(value),
            ])
            .select_from(
                tenant_tbl
                .join(
                    endpoint_sip_section_tbl,
                    endpoint_sip_section_tbl.c.endpoint_sip_uuid == tenant_tbl.c.webrtc_sip_template_uuid,
                )
            )
            .where(endpoint_sip_section_tbl.c.type == 'endpoint')
        )

        query = (
            endpoint_sip_section_option_tbl
            .insert()
            .from_select(
                ['endpoint_sip_section_uuid', 'key', 'value'],
                endpoint_sip_options_insert_subquery
            )
        )
        op.execute(query)


def move_templates_inheriting_from_webrtc_video_to_webrtc():
    query = (
        sql.select([
            tenant_tbl.c.webrtc_video_sip_template_uuid,
            tenant_tbl.c.webrtc_sip_template_uuid,
        ])
    )
    templates = op.get_bind().execute(query)

    for webrtc_video_uuid, webrtc_uuid in templates:
        templates_inheriting_webrtc_subquery = (
            sql.select([
                endpoint_sip_template_tbl.c.child_uuid
            ]).where(
                endpoint_sip_template_tbl.c.parent_uuid == webrtc_uuid,
            )
        )
        query = (
            endpoint_sip_template_tbl.update()
            .values(
                parent_uuid=webrtc_uuid,
            )
            .where(endpoint_sip_template_tbl.c.parent_uuid == webrtc_video_uuid)
            .where(
                sql.not_(endpoint_sip_template_tbl.c.child_uuid.in_(templates_inheriting_webrtc_subquery))
            )
        )
        op.execute(query)


def delete_webrtc_video_template_if_default_values():
    sip_template_with_only_2_options = (
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
        .group_by(endpoint_sip_tbl.c.uuid)
        .having(sql.func.count(endpoint_sip_section_option_tbl.c.uuid) == 2)
    )
    sip_template_with_25_video_streams = (
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
        .where(endpoint_sip_section_tbl.c.type == 'endpoint')
        .where(endpoint_sip_section_option_tbl.c.key == 'max_video_streams')
        .where(endpoint_sip_section_option_tbl.c.value == '25')
    )
    sip_template_with_1_audio_streams = (
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
        .where(endpoint_sip_section_tbl.c.type == 'endpoint')
        .where(endpoint_sip_section_option_tbl.c.key == 'max_audio_streams')
        .where(endpoint_sip_section_option_tbl.c.value == '1')
    )
    default_webrtc_video_templates_subquery = (
        sa.sql.select([endpoint_sip_tbl.c.uuid])
        .where(endpoint_sip_tbl.c.template.is_(True))
        .where(endpoint_sip_tbl.c.uuid.in_(sip_template_with_only_2_options))
        .where(endpoint_sip_tbl.c.uuid.in_(sip_template_with_25_video_streams))
        .where(endpoint_sip_tbl.c.uuid.in_(sip_template_with_1_audio_streams))
    )
    query = (
        endpoint_sip_tbl
        .delete()
        .where(endpoint_sip_tbl.c.uuid.in_(
            sql.select([tenant_tbl.c.webrtc_video_sip_template_uuid])
        ))
        .where(endpoint_sip_tbl.c.uuid.in_(default_webrtc_video_templates_subquery))
    )
    op.get_bind().execute(query)


def upgrade():
    reset_or_add_options_to_webrtc_template()
    move_templates_inheriting_from_webrtc_video_to_webrtc()
    delete_webrtc_video_template_if_default_values()
    op.drop_column("tenant", WEBRTC_VIDEO_COLUMN_NAME)


def downgrade():
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

    query = sa.sql.select([tenant_tbl.c.uuid, tenant_tbl.c.webrtc_sip_template_uuid])
    tenants = op.get_bind().execute(query)
    for tenant in tenants:
        configure_tenant(tenant.uuid, tenant.webrtc_sip_template_uuid)
