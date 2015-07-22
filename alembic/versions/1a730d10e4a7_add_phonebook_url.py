"""add phonebook url

Revision ID: 1a730d10e4a7
Revises: 4ee55e5290be

"""

# revision identifiers, used by Alembic.
revision = '1a730d10e4a7'
down_revision = '4ee55e5290be'

from alembic import op
from sqlalchemy import sql

phonebook_url = 'http://localhost/service/ipbx/json.php/private/pbx_services/phonebook'
directories_table = sql.table('directories',
                              sql.column('uri'),
                              sql.column('dirtype'))
cti_directories_table = sql.table('ctidirectories',
                                  sql.column('uri'))


def upgrade():
    op.execute(directories_table
               .update()
               .where(
                   directories_table.c.dirtype == 'phonebook'
               ).values(uri=phonebook_url))
    op.execute(cti_directories_table
               .update()
               .where(
                   cti_directories_table.c.uri == 'phonebook'
               ).values(uri=phonebook_url))


def downgrade():
    op.execute(directories_table
               .update()
               .where(
                   directories_table.c.uri == phonebook_url
               ).values(uri='phonebook'))
    op.execute(cti_directories_table
               .update()
               .where(
                   cti_directories_table.c.uri == phonebook_url
               ).values(uri='phonebook'))
