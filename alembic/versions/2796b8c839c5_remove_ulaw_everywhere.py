"""remove ulaw everywhere

Revision ID: 2796b8c839c5
Revises: 330b1c94980d

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2796b8c839c5'
down_revision = '330b1c94980d'

endpoint_sip_tbl = sa.sql.table(
    'endpoint_sip',
    sa.sql.column('uuid'),
    sa.sql.column('name'),
)
endpoint_sip_section_tbl = sa.sql.table(
    'endpoint_sip_section',
    sa.sql.column('uuid'),
    sa.sql.column('type'),
    sa.sql.column('endpoint_sip_uuid'),
)
endpoint_sip_section_option_tbl = sa.sql.table(
    'endpoint_sip_section_option',
    sa.sql.column('value'),
    sa.sql.column('key'),
    sa.sql.column('endpoint_sip_section_uuid'),
)

user_sip_tbl = sa.sql.table(
    'usersip',
    sa.sql.column('name'),
    sa.sql.column('allow'),
)

def list_endpoints_with_no_codecs():
    query = sa.sql.select([user_sip_tbl.c.name]).where(sa.sql.and_(
        user_sip_tbl.c.allow != None,
    ))
    return [row.name for row in op.get_bind().execute(query)]


def list_endpoints_with_ulaw():
    query = sa.sql.select(
        [endpoint_sip_tbl.c.name]
    ).select_from(
        endpoint_sip_tbl.join(
            endpoint_sip_section_tbl,
            endpoint_sip_section_tbl.c.endpoint_sip_uuid == endpoint_sip_tbl.c.uuid,
        ).join(
            endpoint_sip_section_option_tbl,
            endpoint_sip_section_option_tbl.c.endpoint_sip_section_uuid == endpoint_sip_section_tbl.c.uuid,
        )
    ).where(endpoint_sip_section_option_tbl.c.value == '!all,ulaw')

    return [row.name for row in op.get_bind().execute(query)]


def remove_codecs(name):
    query = sa.sql.select(
        [endpoint_sip_section_tbl.c.uuid]
    ).select_from(
        endpoint_sip_tbl.join(
            endpoint_sip_section_tbl,
            endpoint_sip_section_tbl.c.endpoint_sip_uuid == endpoint_sip_tbl.c.uuid,
        ).join(
            endpoint_sip_section_option_tbl,
            endpoint_sip_section_option_tbl.c.endpoint_sip_section_uuid == endpoint_sip_section_tbl.c.uuid,
        )
    ).where(
        endpoint_sip_section_tbl.c.type == 'endpoint',
    ).where(
        endpoint_sip_tbl.c.name == name,
    ).group_by(endpoint_sip_section_tbl.c.uuid)

    for row in op.get_bind().execute(query):
        query = endpoint_sip_section_option_tbl.delete().where(
            endpoint_sip_section_option_tbl.c.endpoint_sip_section_uuid == row.uuid,
        ).where(
            endpoint_sip_section_option_tbl.c.key == 'allow',
        ).where(
            endpoint_sip_section_option_tbl.c.value == '!all,ulaw',
        )
        op.execute(query)


def upgrade():
    endpoints_with_no_codecs = set(list_endpoints_with_no_codecs())
    endpoints_with_ulaw_only = set(list_endpoints_with_ulaw())

    endpoints_to_fix = endpoints_with_ulaw_only.intersection(endpoints_with_no_codecs)

    for name in endpoints_to_fix:
        remove_codecs(name)


def downgrade():
    pass
