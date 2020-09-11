"""fix trunk with host migration

Revision ID: 73166af50deb
Revises: 45ec6bd040ac

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73166af50deb'
down_revision = '45ec6bd040ac'

user_sip_tbl = sa.sql.table(
    'usersip',
    sa.sql.column('name'),
    sa.sql.column('category'),
    sa.sql.column('host'),
    sa.sql.column('username'),
    sa.sql.column('port'),
)
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
    sa.sql.column('uuid'),
    sa.sql.column('key'),
    sa.sql.column('value'),
    sa.sql.column('endpoint_sip_section_uuid'),
)


def get_trunk_with_host():
    query = sa.sql.select([
        user_sip_tbl.c.name,
        user_sip_tbl.c.host,
        user_sip_tbl.c.username,
        user_sip_tbl.c.port,
    ]).where(
        sa.and_(
            user_sip_tbl.c.category == 'trunk',
            user_sip_tbl.c.host != 'dynamic',
        )
    )
    rows = op.get_bind().execute(query)
    return [{
        'name': row.name,
        'host': row.host,
        'username': row.username,
        'port': row.port,
    } for row in rows]


def convert_host_to_contact(trunk):
    result = 'sip:'

    username = trunk.get('username')
    if username:
        result += username + '@'

    result += trunk['host']
    port = trunk.get('port') or '5060'
    result += ':' + port
    return result


def find_endpoint_sip(trunk):
    query = sa.sql.select([
        endpoint_sip_tbl.c.uuid
    ]).where(endpoint_sip_tbl.c.name == trunk['name'])
    for row in op.get_bind().execute(query):
        return row.uuid


def find_aor_section(endpoint_uuid):
    query = sa.sql.select([
        endpoint_sip_section_tbl.c.uuid
    ]).where(sa.and_(
        endpoint_sip_section_tbl.c.type == 'aor',
        endpoint_sip_section_tbl.c.endpoint_sip_uuid == endpoint_uuid,
    ))
    for row in op.get_bind().execute(query):
        return row.uuid


def create_aor_section(endpoint_uuid):
    query = endpoint_sip_section_tbl.insert().returning(
        endpoint_sip_section_tbl.c.uuid,
    ).values(
        endpoint_sip_uuid=endpoint_uuid,
        type='aor',
    )
    return op.get_bind().execute(query).scalar()


def add_section_option(section_uuid, key, value):
    query = endpoint_sip_section_option_tbl.insert().values(
        key=key, value=value, endpoint_sip_section_uuid=section_uuid,
    )
    op.execute(query)


def add_contact_to_endpoint(endpoint_uuid, contact):
    aor_section_uuid = find_aor_section(endpoint_uuid)
    if not aor_section_uuid:
        aor_section_uuid = create_aor_section(endpoint_uuid)

    add_section_option(aor_section_uuid, 'contact', contact)


def upgrade():
    trunks_with_host = get_trunk_with_host()
    for trunk in trunks_with_host:
        matching_endpoint_uuid = find_endpoint_sip(trunk)
        if not matching_endpoint_uuid:
            continue
        contact = convert_host_to_contact(trunk)
        add_contact_to_endpoint(matching_endpoint_uuid, contact)


def downgrade():
    pass
