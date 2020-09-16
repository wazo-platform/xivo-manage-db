"""add-missing-pjsip-options

Revision ID: da53b63d9433
Revises: ea9cdf2d59f8

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da53b63d9433'
down_revision = 'ea9cdf2d59f8'

user_sip_tbl = sa.sql.table(
    'usersip',
    sa.sql.column('name'),
    sa.sql.column('category'),
    sa.sql.column('options'),
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

IDENTIFY = 'identify'
REGISTRATION = 'registration'
MISSING_OPTIONS = {
    'srv_lookups': IDENTIFY,
    'match_header': IDENTIFY,
    'contact_header_params': REGISTRATION,
    'forbidden_retry_interval': REGISTRATION,
    'fatal_retry_interval': REGISTRATION,
    'line': REGISTRATION,
    'server_uri': REGISTRATION,
    'support_path': REGISTRATION,
    'support_outbound': REGISTRATION,
}


def get_trunks_with_options():
    query = sa.sql.select([
        user_sip_tbl.c.name,
        user_sip_tbl.c.options,
    ]).where(
        sa.and_(
            user_sip_tbl.c.category == 'trunk',
        )
    )
    rows = op.get_bind().execute(query)
    return [{
        'name': row.name,
        'options': row.options,
    } for row in rows]


def find_missing_trunk_options(trunk):
    missing = {IDENTIFY: [], REGISTRATION: []}
    for key, section in MISSING_OPTIONS.items():
        for option, value in trunk['options']:
            if option == key:
                missing[section].append([key, value])
    return missing


def find_endpoint_uuid(name):
    query = sa.sql.select([
        endpoint_sip_tbl.c.uuid
    ]).where(endpoint_sip_tbl.c.name == name)
    for row in op.get_bind().execute(query):
        return row.uuid


def add_section_option(section_uuid, key, value):
    query = endpoint_sip_section_option_tbl.insert().values(
        key=key, value=value, endpoint_sip_section_uuid=section_uuid,
    )
    op.execute(query)


def find_section(endpoint_uuid, section):
    query = sa.sql.select([
        endpoint_sip_section_tbl.c.uuid
    ]).where(sa.and_(
        endpoint_sip_section_tbl.c.type == section,
        endpoint_sip_section_tbl.c.endpoint_sip_uuid == endpoint_uuid,
    ))
    for row in op.get_bind().execute(query):
        return row.uuid


def create_section(endpoint_uuid, section):
    query = endpoint_sip_section_tbl.insert().returning(
        endpoint_sip_section_tbl.c.uuid,
    ).values(
        endpoint_sip_uuid=endpoint_uuid,
        type=section,
    )
    return op.get_bind().execute(query).scalar()


def find_or_create_section(endpoint_uuid, name):
    section_uuid = find_section(endpoint_uuid, name)
    if not section_uuid:
        section_uuid = create_section(endpoint_uuid, name)
    return section_uuid


def insert_missing_options(name, options):
    if not options[REGISTRATION] and not options[IDENTIFY]:
        return

    endpoint_uuid = find_endpoint_uuid(name)

    if options[IDENTIFY]:
        identify_section_uuid = find_or_create_section(endpoint_uuid, IDENTIFY)
        for key, value in options[IDENTIFY]:
            add_section_option(identify_section_uuid, key, value)

    if options[REGISTRATION]:
        registration_section_uuid = find_or_create_section(endpoint_uuid, REGISTRATION)
        for key, value in options[REGISTRATION]:
            add_section_option(registration_section_uuid, key, value)


def upgrade():
    trunks = get_trunks_with_options()
    for trunk in trunks:
        to_insert = find_missing_trunk_options(trunk)
        insert_missing_options(trunk['name'], to_insert)


def downgrade():
    pass
