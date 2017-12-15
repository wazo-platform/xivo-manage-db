"""populate-confbridge-configuration

Revision ID: 55f7b6c13454
Revises: 488e5a3d75

"""

# revision identifiers, used by Alembic.
revision = '55f7b6c13454'
down_revision = '488e5a3d75'

from alembic import op
import sqlalchemy as sa

asterisk_file_table = sa.sql.table('asterisk_file',
                                   sa.sql.column('id'),
                                   sa.sql.column('name'))

asterisk_file_section_table = sa.sql.table('asterisk_file_section',
                                           sa.sql.column('id'),
                                           sa.sql.column('name'),
                                           sa.sql.column('priority'),
                                           sa.sql.column('asterisk_file_id'))

asterisk_file_variable_table = sa.sql.table('asterisk_file_variable',
                                            sa.sql.column('id'),
                                            sa.sql.column('key'),
                                            sa.sql.column('value'),
                                            sa.sql.column('priority'),
                                            sa.sql.column('asterisk_file_section_id'))


def upgrade():
    file_id = _insert_asterisk_file('confbridge.conf')
    _insert_asterisk_file_section(file_id, 'general', priority=0)
    _insert_asterisk_file_section(file_id, 'default_bridge')

    section_id = _insert_asterisk_file_section(file_id, 'default_user')
    _insert_asterisk_file_variable(section_id, 'dsp_drop_silence', 'yes')


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
    op.execute(asterisk_file_table.delete().where(asterisk_file_table.c.name == 'confbridge.conf'))
