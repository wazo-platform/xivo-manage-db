"""rename webservices directory

Revision ID: 444b39e9aa32
Revises: 5ace7dc40b5c

"""

# revision identifiers, used by Alembic.
revision = '444b39e9aa32'
down_revision = '5ace7dc40b5c'

from alembic import op
from sqlalchemy import sql

directories_table = sql.table('directories',
                              sql.column('dirtype'))


def rename_dirtype(from_, to):
    op.execute(directories_table
               .update()
               .where(
                   directories_table.c.dirtype == from_
               ).values(dirtype=to))


def upgrade():
    rename_dirtype(from_='webservices', to='csv_ws')


def downgrade():
    rename_dirtype(from_='csv_ws', to='webservices')
