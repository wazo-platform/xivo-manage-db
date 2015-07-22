"""directories xivo confd uri

Revision ID: 4ee55e5290be
Revises: 41e07bde92da

"""

# revision identifiers, used by Alembic.
revision = '4ee55e5290be'
down_revision = '41e07bde92da'

from alembic import op
from sqlalchemy import sql

confd_url = 'http://localhost:9487'
directories_table = sql.table('directories',
                              sql.column('uri'),
                              sql.column('dirtype'))
cti_directories_table = sql.table('ctidirectories',
                                  sql.column('uri'))


def upgrade():
    op.execute(directories_table
               .update()
               .where(
                   directories_table.c.dirtype == 'xivo'
               ).values(uri=confd_url))
    op.execute(cti_directories_table
               .update()
               .where(
                   cti_directories_table.c.uri == 'xivo'
               ).values(uri=confd_url))


def downgrade():
    op.execute(directories_table
               .update()
               .where(
                   directories_table.c.uri == confd_url
               ).values(uri='xivo'))
    op.execute(cti_directories_table
               .update()
               .where(
                   cti_directories_table.c.uri == confd_url
               ).values(uri='xivo'))
