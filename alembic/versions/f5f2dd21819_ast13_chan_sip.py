"""ast13: remove chan_sip callevents

Revision ID: f5f2dd21819
Revises: 44af2488e95

"""

# revision identifiers, used by Alembic.
revision = 'f5f2dd21819'
down_revision = '44af2488e95'

from alembic import op
from sqlalchemy import sql


staticsip_table = sql.table('staticsip',
                            sql.column('var_name'))


def upgrade():
    _delete_staticsip_callevents()


def _delete_staticsip_callevents():
    op.execute(staticsip_table.delete().where(staticsip_table.c.var_name == 'callevents'))


def downgrade():
    pass
