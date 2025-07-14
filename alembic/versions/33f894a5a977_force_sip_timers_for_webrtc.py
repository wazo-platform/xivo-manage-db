"""Force sip timers for webrtc

Revision ID: 33f894a5a977
Revises: ca4bca36b8ac

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = '33f894a5a977'
down_revision = 'ca4bca36b8ac'


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
    sa.sql.column("webrtc_sip_template_uuid")
)

def get_sip_endpoint_webrtc_templates() -> sa.sql.Selectable:
    query = sa.sql.select([
        endpoint_sip_table.c.uuid,
    ]).select_from(
        endpoint_sip_table.join(
            tenant_table,
            tenant_table.c.webrtc_sip_template_uuid == endpoint_sip_table.c.uuid
        )
    )
    return query


def add_option_where_not_defined(option_key, option_value, endpoint_sip_templates):
    # identify templates with option_key already defined
    # we don't want to overwrite those
    conflicting_templates = sa.sql.select([
        sa.sql.distinct(endpoint_sip_table.c.uuid)
    ]).select_from(
        endpoint_sip_section_option_table.join(
            endpoint_sip_section_table,
            endpoint_sip_section_table.c.uuid ==
            endpoint_sip_section_option_table.c.endpoint_sip_section_uuid
        ).join(
            endpoint_sip_table,
            endpoint_sip_table.c.uuid == endpoint_sip_section_table.c.endpoint_sip_uuid
        )
    ).where(
        sa.sql.and_(
            endpoint_sip_table.c.template,
            endpoint_sip_table.c.uuid.in_(endpoint_sip_templates),
            endpoint_sip_section_table.c.type == 'endpoint',
            endpoint_sip_section_option_table.c.key == option_key,
        )
    )

    return sa.sql.insert(endpoint_sip_section_option_table).from_select(
        [
            'key',
            'value',
            'endpoint_sip_section_uuid'
        ],
        sa.sql.select([
            sa.sql.literal(option_key),
            sa.sql.literal(option_value),
            endpoint_sip_section_table.c.uuid
        ]).where(
            sa.sql.and_(
                endpoint_sip_section_table.c.endpoint_sip_uuid.in_(
                    endpoint_sip_templates.except_(conflicting_templates)
                ),
                endpoint_sip_section_table.c.type == 'endpoint',
            )
        )
    )


def upgrade():
    webrtc_templates = get_sip_endpoint_webrtc_templates()
    _ = op.get_bind().execute(
        add_option_where_not_defined(
            'timers',
            'always',
            webrtc_templates
        )
    )
    _ = op.get_bind().execute(
        add_option_where_not_defined(
            'timers_sess_expires',
            '300',
            webrtc_templates
        )
    )
    _ = op.get_bind().execute(
        add_option_where_not_defined(
            'timers_min_se',
            '90',
            webrtc_templates
        )
    )


def downgrade():
    # cannot know which templates have been touched by upgrade
    pass
