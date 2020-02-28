"""migrate_sip_general_to_pjsip_global

Revision ID: 28195459f3d1
Revises: 6ff776dde35e

"""

from alembic import op
from sqlalchemy import sql


# revision identifiers, used by Alembic.
revision = '28195459f3d1'
down_revision = '6ff776dde35e'

FILENAME = 'pjsip.conf'
DEFAULTS = {
    'endpoint_identifier_order': 'auth_username,username,ip',
    'user_agent': 'Wazo PBX',
}

# Fields that are actually "translated" by wazo-confgend
SIP_TO_PJSIP_MAPPING = {
    'legacy_useroption_parsing': 'ignore_uri_user_options',
    'sipdebug': 'debug',
    'useragent': 'user_agent',
}

# zcat /usr/share/doc/asterisk-doc/json/pjsip.json.gz | jq .global[].name | sort -u
VERBATIM_PJSIP_GLOBAL_OPTIONS = [
    "contact_expiration_check_interval",
    "debug",
    "default_from_user",
    "default_outbound_endpoint",
    "default_realm",
    "default_voicemail_extension",
    "disable_multi_domain",
    "endpoint_identifier_order",
    "ignore_uri_user_options",
    "keep_alive_interval",
    "max_forwards",
    "max_initial_qualify_time",
    "mwi_disable_initial_unsolicited",
    "mwi_tps_queue_high",
    "mwi_tps_queue_low",
    "norefersub",
    "regcontext",
    "send_contact_status_on_update_registration",
    "taskprocessor_overload_trigger",
    "unidentified_request_count",
    "unidentified_request_period",
    "unidentified_request_prune_interval",
    "use_callerid_contact",
    "user_agent",
]

asterisk_file_table = sql.table(
    'asterisk_file',
    sql.column('id'),
    sql.column('name'),
)

asterisk_file_section_table = sql.table(
    'asterisk_file_section',
    sql.column('id'),
    sql.column('name'),
    sql.column('priority'),
    sql.column('asterisk_file_id'),
)

asterisk_file_variable_table = sql.table(
    'asterisk_file_variable',
    sql.column('id'),
    sql.column('key'),
    sql.column('value'),
    sql.column('asterisk_file_section_id'),
)

staticsip_table = sql.table(
    'staticsip',
    sql.column('var_name'),
    sql.column('var_val'),
)


def upgrade():
    file_id = _insert_asterisk_file(FILENAME)
    section_id = _insert_asterisk_file_section(file_id, 'global', priority=0)
    current_sip_options = _get_current_sip_options()

    global_options = dict(DEFAULTS)

    for var, val in current_sip_options.items():
        # Add options mapped from sip.conf
        if var in SIP_TO_PJSIP_MAPPING:
            global_options[SIP_TO_PJSIP_MAPPING[var]] = val

        # If the admin used pjsip.conf keys
        if var in VERBATIM_PJSIP_GLOBAL_OPTIONS:
            global_options[var] = val

    for var, value in global_options.items():
        # We used to store null values in the db to match the form in the UI, not anymore.
        if value is None:
            continue
        _insert_asterisk_file_variable(section_id, var, value)


def _get_current_sip_options():
    query = (sql.select([staticsip_table.c.var_name, staticsip_table.c.var_val]))
    return {row[0]: row[1] for row in op.get_bind().execute(query)}


def _insert_asterisk_file(name):
    query = (asterisk_file_table
             .insert()
             .returning(asterisk_file_table.c.id)
             .values(name=name))

    return op.get_bind().execute(query).scalar()


def _insert_asterisk_file_section(file_id, name, priority=None):
    query = (asterisk_file_section_table
             .insert()
             .returning(asterisk_file_section_table.c.id)
             .values(name=name,
                     priority=priority,
                     asterisk_file_id=file_id))

    return op.get_bind().execute(query).scalar()


def _insert_asterisk_file_variable(section_id, key, value):
    query = (asterisk_file_variable_table
             .insert()
             .values(key=key,
                     value=value,
                     asterisk_file_section_id=section_id))

    op.execute(query)


def downgrade():
    op.execute(asterisk_file_table.delete().where(asterisk_file_table.c.name == FILENAME))
