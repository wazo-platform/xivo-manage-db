"""phonebook file to csv

Revision ID: 40ba1a488aa7
Revises: 1a730d10e4a7

"""

# revision identifiers, used by Alembic.
revision = '40ba1a488aa7'
down_revision = '1a730d10e4a7'

from alembic import op
from sqlalchemy import sql

directories_table = sql.table('directories',
                              sql.column('dirtype'))


def upgrade():
    op.execute(directories_table
               .update()
               .where(
                   directories_table.c.dirtype == 'file'
               ).values(dirtype='csv'))


def downgrade():
    op.execute(directories_table
               .update()
               .where(
                   directories_table.c.dirtype == 'csv'
               ).values(dirtype='file'))
