"""rtp_general_section

Revision ID: ee27cd6ccd9
Revises: 4e2fb3cbc2a2

"""

from alembic import op
from sqlalchemy import sql


# revision identifiers, used by Alembic.
revision = 'ee27cd6ccd9'
down_revision = '4e2fb3cbc2a2'

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


def upgrade():
    file_id = _insert_asterisk_file('rtp.conf')

    section_id = _insert_asterisk_file_section(file_id, 'general', priority=0)
    _insert_asterisk_file_variable(section_id, 'rtpstart', '10000')
    _insert_asterisk_file_variable(section_id, 'rtpend', '20000')

    _insert_asterisk_file_section(file_id, 'ice_host_candidates')


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

    op.get_bind().execute(query)


def downgrade():
    op.execute(asterisk_file_table.delete().where(asterisk_file_table.c.name == 'rtp.conf'))
