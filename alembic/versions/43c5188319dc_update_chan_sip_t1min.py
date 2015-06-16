"""update chan_sip t1min

Revision ID: 43c5188319dc
Revises: 160e7b3161fa

"""

# revision identifiers, used by Alembic.
revision = '43c5188319dc'
down_revision = '160e7b3161fa'

from alembic import op
from sqlalchemy import sql


staticsip_table = sql.table('staticsip',
                            sql.column('var_name'),
                            sql.column('var_val'))


def upgrade():
    _update_staticsip_t1min()


def _update_staticsip_t1min():
    op.execute(staticsip_table.update().
               where(sql.and_(
                   staticsip_table.c.var_name == 't1min',
                   staticsip_table.c.var_val == '100')).
               values(var_val='500'))


def downgrade():
    pass
