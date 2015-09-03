"""remove remotedirectory xlet

Revision ID: 1632064e0441
Revises: 337f76c25478

"""

# revision identifiers, used by Alembic.
revision = '1632064e0441'
down_revision = '337f76c25478'

from alembic import op
from sqlalchemy import sql


xlet_table = sql.table('cti_xlet',
                       sql.column('id'),
                       sql.column('plugin_name'))


def upgrade():
    op.execute(xlet_table.delete().where(xlet_table.c.plugin_name == 'remotedirectory'))


def downgrade():
    op.execute(xlet_table.insert().values(plugin_name='remotedirectory'))
