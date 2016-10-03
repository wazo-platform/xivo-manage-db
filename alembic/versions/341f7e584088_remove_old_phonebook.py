"""remove old phonebook

Revision ID: 341f7e584088
Revises: 43a39441ae83

"""

# revision identifiers, used by Alembic.
revision = '341f7e584088'
down_revision = '43a39441ae83'

from alembic import op
from sqlalchemy import sql

cti_directory_fields = sql.table('ctidirectoryfields', sql.column('dir_id'))
cti_directories = sql.table('ctidirectories', sql.column('id'))
directories = sql.table('directories', sql.column('dirtype'))


def upgrade():
    conn = op.get_bind()

    remove_unused_fields(conn)
    op.create_foreign_key('ctidirectoryfields_dir_id_fkey',
                          'ctidirectoryfields', 'ctidirectories',
                          ['dir_id'], ['id'],
                          ondelete='CASCADE')

    op.execute(directories.delete()
                          .where(directories.c.dirtype == 'phonebook'))


def downgrade():
    pass


def remove_unused_fields(conn):
    query = sql.select([cti_directories])
    ids = [d.id for d in conn.execute(query)]
    op.execute(cti_directory_fields.delete()
                                   .where(~cti_directory_fields.c.dir_id.in_(ids)))
