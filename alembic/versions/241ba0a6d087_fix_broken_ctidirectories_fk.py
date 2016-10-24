"""fix broken ctidirectories fk

Revision ID: 241ba0a6d087
Revises: 15b236bd8060

"""

# revision identifiers, used by Alembic.
revision = '241ba0a6d087'
down_revision = '15b236bd8060'

from alembic import op
import sqlalchemy as sa

cti_directories_table = sa.sql.table('ctidirectories',
                                     sa.Column('id'),
                                     sa.Column('name'),
                                     sa.Column('directory_id'))
directory_table = sa.sql.table('directories',
                               sa.Column('id'),
                               sa.Column('name'))


def get_directory_id_map(conn):
    query = sa.sql.select([directory_table])
    return {d.name: d.id for d in conn.execute(query)}


def get_cti_directory_id_map(conn):
    query = sa.sql.select([cti_directories_table])
    return {d.name: d.id for d in conn.execute(query)}


def associate_cti_directory_to_directory(cti_directory_id, directory_id):
    if not cti_directory_id or not directory_id:
        return

    op.execute(
        cti_directories_table
        .update()
        .where(cti_directories_table.c.id == cti_directory_id)
        .values(directory_id=directory_id)
    )


def upgrade():
    conn = op.get_bind()

    directory_id_map = get_directory_id_map(conn)
    cti_directory_id_map = get_cti_directory_id_map(conn)

    associate_cti_directory_to_directory(cti_directory_id_map.get('xivodir'),
                                         directory_id_map.get('phonebook'))

    associate_cti_directory_to_directory(cti_directory_id_map.get('internal'),
                                         directory_id_map.get('xivo'))


def downgrade():
    pass
