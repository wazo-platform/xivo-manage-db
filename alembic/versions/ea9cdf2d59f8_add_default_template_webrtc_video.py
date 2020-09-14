"""Add default template webrtc_video

Revision ID: ea9cdf2d59f8
Revises: bf1aaa27b7f8

"""

import string
import random

from collections import namedtuple

from alembic import op
import sqlalchemy as sa
from sqlalchemy import sql

from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = "ea9cdf2d59f8"
down_revision = "bf1aaa27b7f8"

ALPHANUMERIC_POOL = string.ascii_lowercase + string.digits
KV = namedtuple("KV", ["key", "value"])
WEBRTC_VIDEO_COLUMN_NAME = "webrtc_video_sip_template_uuid"

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
    query = sa.sql.select([transport_option_tbl.c.pjsip_transport_uuid]).where(
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


def insert_endpoint_config(tenant_uuid, body, parents=None):
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
    # 1. Create default template and assign to tenant
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

    # 2. Find sip endpoint with matching params
    endpoint_uuids = []
    endpoints = (
        sa.sql.select([endpoint_sip_tbl.c.uuid])
        .where(endpoint_sip_tbl.c.template.is_(False))
        .where(endpoint_sip_tbl.c.tenant_uuid == tenant_uuid)
    )

    for endpoint in op.get_bind().execute(endpoints):
        endpoint_uuid = endpoint[0]

        # 2.1 Fetch endpoint_section
        sections = (
            sa.sql.select([endpoint_sip_section_tbl.c.uuid])
            .where(endpoint_sip_section_tbl.c.type == 'endpoint')
            .where(endpoint_sip_section_tbl.c.endpoint_sip_uuid == endpoint_uuid)
        )

        for section in op.get_bind().execute(sections):
            section_uuid = section[0]

            # 2.2 Fetch options
            sections = (
                sa.sql.select([sa.func.count(endpoint_sip_section_option_tbl.c.key)])
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
                .where(endpoint_sip_section_option_tbl.c.endpoint_sip_section_uuid == section_uuid)
                .group_by(endpoint_sip_section_option_tbl.c.endpoint_sip_section_uuid)
            )

            options_count = op.get_bind().execute(sections).scalar()
            # 2.3 Store endpoint uuid
            if options_count == 2:
                endpoint_uuids.append(endpoint_uuid)

    # 3. Assign webrtc_video template to endpoints
    for endpoint_uuid in endpoint_uuids:
        query = endpoint_sip_template_tbl.insert().values(
            child_uuid=endpoint_uuid,
            parent_uuid=webrtc_video_config["uuid"],
        )
        op.execute(query)


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

    # 5. Delete options matching default params
    delete_query = (
        endpoint_sip_section_option_tbl.delete()
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

    op.get_bind().execute(delete_query)


def downgrade():
    # 1. Drop templates webrtc_video
    query = endpoint_sip_tbl.delete().where(endpoint_sip_tbl.c.label == "webrtc_video")

    op.get_bind().execute(query)

    # 2. Drop table column
    op.drop_column("tenant", WEBRTC_VIDEO_COLUMN_NAME)
