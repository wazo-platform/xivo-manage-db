"""add-pjsip-system

Revision ID: 1c95890bb00d
Revises: 28195459f3d1

"""

from alembic import op
from sqlalchemy import sql

# revision identifiers, used by Alembic.
revision = '1c95890bb00d'
down_revision = '28195459f3d1'

FILENAME = 'pjsip.conf'
DEFAULTS = {}

# Fields that are actually "translated" by wazo-confgend
SIP_TO_PJSIP_MAPPING = {
    'timert1': 'timer_t1',
    'timerb': 'timer_b',
    'compactheaders': 'compact_headers',
}

# zcat /usr/share/doc/asterisk-doc/json/pjsip.json.gz | jq .system[].name | sort -u
VERBATIM_PJSIP_SYSTEM_OPTIONS = [
    "accept_multiple_sdp_answers",
    "compact_headers",
    "disable_tcp_switch",
    "follow_early_media_fork",
    "threadpool_auto_increment",
    "threadpool_idle_timeout",
    "threadpool_initial_size",
    "threadpool_max_size",
    "timer_b",
    "timer_t1",
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
    file_id = _find_asterisk_file_id(FILENAME)
    section_id = _insert_asterisk_file_section(file_id, 'system', priority=0)
    current_sip_options = _get_current_sip_options()

    system_options = dict(DEFAULTS)

    for var, val in current_sip_options.items():
        # Add options mapped from sip.conf
        if var in SIP_TO_PJSIP_MAPPING:
            system_options[SIP_TO_PJSIP_MAPPING[var]] = val

        # If the admin used pjsip.conf keys
        if var in VERBATIM_PJSIP_SYSTEM_OPTIONS:
            system_options[var] = val

    for var, value in system_options.items():
        # We used to store null values in the db to match the form in the UI, not anymore.
        if value is None:
            continue
        _insert_asterisk_file_variable(section_id, var, value)


def _get_current_sip_options():
    query = (sql.select([staticsip_table.c.var_name, staticsip_table.c.var_val]))
    return {row[0]: row[1] for row in op.get_bind().execute(query)}


def _find_asterisk_file_id(name):
    query = sql.select(
        [asterisk_file_table.c.id]
    ).where(asterisk_file_table.c.name == name)
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
    file_id = _find_asterisk_file_id(FILENAME)
    op.execute(asterisk_file_section_table.delete().where(
        sql.and_(
            asterisk_file_section_table.c.asterisk_file_id == file_id,
            asterisk_file_section_table.c.name == 'system',
        )
    ))
