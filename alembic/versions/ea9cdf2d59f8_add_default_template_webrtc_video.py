"""Add default template webrtc_video

Revision ID: ea9cdf2d59f8
Revises: f98e74435092

"""

import string
import random

from collections import namedtuple

from alembic import op
import sqlalchemy as sa

from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = "ea9cdf2d59f8"
down_revision = "bba3a031fd01"

WEBRTC_VIDEO_COLUMN_NAME = "webrtc_video_sip_template_uuid"

KV = namedtuple("KV", ["key", "value"])

ALPHANUMERIC_POOL = string.ascii_lowercase + string.digits

transport_option_tbl = sa.sql.table(
    "pjsip_transport_option",
    sa.sql.column("key"),
    sa.sql.column("value"),
    sa.sql.column("pjsip_transport_uuid"),
)
endpoint_sip_tbl = sa.sql.table(
    "endpoint_sip",
    sa.sql.column("uuid"),
    sa.sql.column("label"),
    sa.sql.column("name"),
    sa.sql.column("asterisk_id"),
    sa.sql.column("tenant_uuid"),
    sa.sql.column("transport_uuid"),
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
transport_tbl = sa.sql.table(
    "pjsip_transport",
    sa.sql.column("uuid"),
    sa.sql.column("name"),
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


def find_wss_transport():
    query = sa.sql.select([transport_option_tbl.c.pjsip_transport_uuid,]).where(
        sa.sql.and_(
            transport_option_tbl.c.key == "protocol",
            transport_option_tbl.c.value == "wss",
        )
    )
    rows = op.get_bind().execute(query)
    for row in rows:
        return row.pjsip_transport_uuid


def create_webrtc_video_config_body():
    body = {
        "label": "WebRTC line (Video)",
        "endpoint_section_options": [
            KV("max_video_streams", "25"),
            KV("max_audio_streams", "1"),
        ],
        "template": True,
        "transport_uuid": find_wss_transport(),
    }

    return body


def insert_section(endpoint_sip_uuid, type, options):
    if not options:
        return

    query = (
        endpoint_sip_section_tbl.insert()
        .returning(endpoint_sip_section_tbl.c.uuid)
        .values(
            endpoint_sip_uuid=endpoint_sip_uuid,
            type=type,
        )
    )
    section_uuid = op.get_bind().execute(query).scalar()

    for key, value in options:
        query = endpoint_sip_section_option_tbl.insert().values(
            key=key,
            value=value,
            endpoint_sip_section_uuid=section_uuid,
        )
        op.execute(query)

    return section_uuid


def insert_endpoint_config(
    tenant_uuid,
    body,
    parents=None,
):
    aor_section_options = body.get("aor_section_options")
    auth_section_options = body.get("auth_section_options")
    endpoint_section_options = body.get("endpoint_section_options")
    identify_section_options = body.get("identify_section_options")
    registration_section_options = body.get("registration_section_options")
    outbound_auth_section_options = body.get("outbound_auth_section_options")
    registration_outbound_auth_section_options = body.get(
        "registration_outbound_auth_section_options"
    )

    query = (
        endpoint_sip_tbl.insert()
        .returning(endpoint_sip_tbl.c.uuid)
        .values(
            label=body["label"],
            name=body.get("name") or generate_unused_name(),
            tenant_uuid=tenant_uuid,
            template=body.get("template", False),
            transport_uuid=body.get("transport_uuid"),
        )
    )
    body["uuid"] = op.get_bind().execute(query).scalar()
    insert_section(body["uuid"], "aor", aor_section_options)
    insert_section(body["uuid"], "auth", auth_section_options)
    insert_section(body["uuid"], "endpoint", endpoint_section_options)
    insert_section(body["uuid"], "identify", identify_section_options)
    insert_section(body["uuid"], "registration", registration_section_options)
    insert_section(
        body["uuid"],
        "registration_outbound_auth",
        registration_outbound_auth_section_options,
    )
    insert_section(body["uuid"], "outbound_auth", outbound_auth_section_options)

    for parent in parents or []:
        query = endpoint_sip_template_tbl.insert().values(
            child_uuid=body["uuid"],
            parent_uuid=parent["uuid"],
        )
        op.execute(query)

    return body


def get_transports():
    query = sa.sql.select([transport_tbl.c.uuid, transport_tbl.c.name])
    rows = op.get_bind().execute(query)
    return {row.name: row.uuid for row in rows}


def insert_webrtc_video_config(tenant_uuid, parents, body):
    body.update(
        {
            "label": "webrtc_video",
            "template": True,
        }
    )
    return insert_endpoint_config(tenant_uuid, body, parents)


def configure_tenant(
    tenant_uuid,
    webrtc_sip_template_uuid,
    webrtc_video_config_body,
    transports,
    tenant_tbl,
):
    webrtc_config = {"uuid": webrtc_sip_template_uuid}
    webrtc_video_config = insert_webrtc_video_config(
        tenant_uuid,
        parents=[webrtc_config],
        body=webrtc_video_config_body,
    )

    op.execute(
        tenant_tbl.update()
        .values(
            webrtc_video_sip_template_uuid=webrtc_video_config["uuid"],
        )
        .where(tenant_tbl.c.uuid == tenant_uuid)
    )

    # line_configs = list_existing_line_config(tenant_uuid)
    # for line_config in line_configs:
    #     configure_line(tenant_uuid, global_config, webrtc_config, line_config, transports)


def list_tenants(tenant_tbl):
    query = sa.sql.select(
        [
            tenant_tbl.c.uuid,
            tenant_tbl.c.webrtc_sip_template_uuid,
            tenant_tbl.c.webrtc_video_sip_template_uuid,
        ]
    )
    tenants = []

    for row in op.get_bind().execute(query):
        tenants.append(
            {
                "uuid": row[0],
                "webrtc_sip_template_uuid": row[1],
                "webrtc_video_sip_template_uuid": row[2],
            }
        )
    return tenants


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

    # 2. Init tenant table and fetch
    tenant_tbl = sa.sql.table(
        "tenant",
        sa.sql.column("uuid"),
        sa.sql.column("webrtc_sip_template_uuid"),
        sa.sql.column(WEBRTC_VIDEO_COLUMN_NAME),
    )
    transports = get_transports()

    # 3. Create new template
    webrtc_video_config_body = create_webrtc_video_config_body()

    # 4. Assign template to tenants
    for tenant in list_tenants(tenant_tbl):
        configure_tenant(
            tenant["uuid"],
            tenant["webrtc_sip_template_uuid"],
            webrtc_video_config_body,
            transports,
            tenant_tbl,
        )


def downgrade():
    # 1. Drop templates webrtc_video
    query = endpoint_sip_tbl.delete().where(endpoint_sip_tbl.c.label == "webrtc_video")

    op.get_bind().execute(query)

    # 2. Drop table column
    op.drop_column("tenant", WEBRTC_VIDEO_COLUMN_NAME)
