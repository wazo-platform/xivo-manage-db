"""hep general section

Revision ID: 62c5befaa8cf
Revises: 87b36150b613

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62c5befaa8cf'
down_revision = '87b36150b613'


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
    file_id = _insert_asterisk_file('hep.conf')

    section_id = _insert_asterisk_file_section(file_id, 'general', priority=0)
    _insert_asterisk_file_variable(section_id, 'enabled', '0')


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
    op.execute(asterisk_file_table.delete().where(asterisk_file_table.c.name == 'hep.conf'))
