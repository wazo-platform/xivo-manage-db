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


def remove_from_profile():
    xlet_id_query = (sa.sql.select([xlet_table.c.id])
                     .where(xlet_table.c.plugin_name == DIAL_XLET))
    xlet_id = op.get_bind().execute(xlet_id_query).scalar()

    remove_from_profile_query = (profile_xlet_table
                                 .delete()
                                 .where(profile_xlet_table.c.xlet_id == xlet_id))
    op.execute(remove_from_profile_query)


def create_xlet():
    create_xlet_query = (xlet_table
                         .insert()
                         .values(plugin_name=DIAL_XLET))
    op.execute(create_xlet_query)


def upgrade():
    remove_from_profile()
    remove_xlet()


def downgrade():
    create_xlet()
