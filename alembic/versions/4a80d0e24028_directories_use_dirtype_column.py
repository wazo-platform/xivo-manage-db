"""directories use dirtype column

Revision ID: 4a80d0e24028
Revises: 151d1315479b

"""

# revision identifiers, used by Alembic.
revision = '4a80d0e24028'
down_revision = '151d1315479b'

from alembic import op
from sqlalchemy import sql

directories_table = sql.table('directories',
                              sql.column('uri'),
                              sql.column('id'),
                              sql.column('dirtype'))


def update_dirtype(uri_pattern, dirtype):
    op.execute(directories_table
               .update()
               .where(
                   directories_table.c.uri.like(uri_pattern)
               )
               .values(dirtype=dirtype))


def drop_all_dirtype():
    op.execute(directories_table.update().values(dirtype=''))


def update_phonebook():
    update_dirtype('phonebook', 'phonebook')


def update_internal():
    update_dirtype('internal', 'internal')


def update_file():
    update_dirtype('file://%', 'file')


def update_ws():
    op.execute(directories_table
               .update()
               .where(directories_table.c.dirtype == '')
               .values(dirtype='webservices'))


def add_not_null_constraint():
    op.alter_column('directories', 'dirtype', nullable=False)


def remove_not_null_constraint():
    op.alter_column('directories', 'dirtype', nullable=True)


def upgrade():
    update_phonebook()
    update_internal()
    update_file()
    update_ws()
    add_not_null_constraint()


def downgrade():
    remove_not_null_constraint()
    drop_all_dirtype()
