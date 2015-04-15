"""remove dialer xlet

Revision ID: 2956eaa19c7c
Revises: 534d6112e879

"""

# revision identifiers, used by Alembic.
revision = '2956eaa19c7c'
down_revision = '534d6112e879'

from alembic import op
import sqlalchemy as sa


DIAL_XLET = 'dial'


xlet_table = sa.sql.table('cti_xlet',
                          sa.sql.column('id'),
                          sa.sql.column('plugin_name'))
profile_xlet_table = sa.sql.table('cti_profile_xlet',
                                  sa.sql.column('xlet_id'))


def remove_xlet():
    remove_xlet_query = (xlet_table
                         .delete()
                         .where(xlet_table.c.plugin_name == DIAL_XLET))
    op.execute(remove_xlet_query)


def create_xlet():
    create_xlet_query = (xlet_table
                         .insert()
                         .values(plugin_name=DIAL_XLET))
    op.execute(create_xlet_query)


def upgrade():
    remove_xlet()


def downgrade():
    create_xlet()
