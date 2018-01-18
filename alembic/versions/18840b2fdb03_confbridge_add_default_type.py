"""confbridge_add_default_type

Revision ID: 18840b2fdb03
Revises: 505c12d2ed73

"""

# revision identifiers, used by Alembic.
revision = '18840b2fdb03'
down_revision = '505c12d2ed73'

from alembic import op
from sqlalchemy import sql

asterisk_file_table = sql.table('asterisk_file',
                                sql.column('id'),
                                sql.column('name'))

asterisk_file_section_table = sql.table('asterisk_file_section',
                                        sql.column('id'),
                                        sql.column('name'),
                                        sql.column('asterisk_file_id'))

asterisk_file_variable_table = sql.table('asterisk_file_variable',
                                         sql.column('id'),
                                         sql.column('key'),
                                         sql.column('value'),
                                         sql.column('asterisk_file_section_id'))


def upgrade():
    file_id = _get_asterisk_file_id('confbridge.conf')

    section_id = _rename_asterisk_file_section(file_id, 'default_bridge', 'wazo_default_bridge')
    _insert_asterisk_file_variable(section_id, 'type', 'bridge')

    section_id = _rename_asterisk_file_section(file_id, 'default_user', 'wazo_default_user')
    _insert_asterisk_file_variable(section_id, 'type', 'user')


def _get_asterisk_file_id(file_name):
    query = (sql.select([asterisk_file_table.c.id])
             .where(asterisk_file_table.c.name == file_name))
    for result in op.get_bind().execute(query):
        return result.id


def _rename_asterisk_file_section(file_id, old_name, new_name):
    query = (asterisk_file_section_table
             .update()
             .returning(asterisk_file_section_table.c.id)
             .where(sql.and_(
                 asterisk_file_section_table.c.asterisk_file_id == file_id,
                 asterisk_file_section_table.c.name == old_name,
             ))
             .values(name=new_name))

    for result in op.get_bind().execute(query):
        return result.id


def _insert_asterisk_file_variable(section_id, key, value):
    query = (asterisk_file_variable_table
             .insert()
             .values(key=key,
                     value=value,
                     asterisk_file_section_id=section_id))

    op.get_bind().execute(query)


def downgrade():
    file_id = _get_asterisk_file_id('confbridge.conf')

    section_id = _rename_asterisk_file_section(file_id, 'wazo_default_bridge', 'default_bridge')
    _remove_asterisk_file_variable(section_id, 'type', 'bridge')

    section_id = _rename_asterisk_file_section(file_id, 'wazo_default_user', 'default_user')
    _remove_asterisk_file_variable(section_id, 'type', 'user')


def _remove_asterisk_file_variable(section_id, key, value):
    query = (asterisk_file_variable_table
             .delete()
             .where(sql.and_(
                 asterisk_file_variable_table.c.key == key,
                 asterisk_file_variable_table.c.value == value,
                 asterisk_file_variable_table.c.asterisk_file_section_id == section_id
             )))

    op.get_bind().execute(query)
