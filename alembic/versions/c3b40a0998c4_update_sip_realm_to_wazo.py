"""update_sip_realm_to_wazo

Revision ID: c3b40a0998c4
Revises: 30d7dcbb9133

"""

# revision identifiers, used by Alembic.
revision = 'c3b40a0998c4'
down_revision = '30d7dcbb9133'

from alembic import op
from sqlalchemy import sql, func


staticsip = sql.table('staticsip',
                      sql.column('var_name'),
                      sql.column('var_val'))


def upgrade():
    query = (staticsip
             .update()
             .values(var_val='wazo')
             .where(sql.and_(
                 staticsip.c.var_name == "realm",
                 func.lower(staticsip.c.var_val) == "xivo")))
    op.execute(query)


def downgrade():
    query = (staticsip
             .update()
             .values(var_val='xivo')
             .where(sql.and_(
                 staticsip.c.var_name == "realm",
                 func.lower(staticsip.c.var_val) == "wazo")))
    op.execute(query)
