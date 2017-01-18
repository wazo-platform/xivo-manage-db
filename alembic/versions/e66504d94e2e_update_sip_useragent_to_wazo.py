"""update_sip_useragent_to_wazo

Revision ID: e66504d94e2e
Revises: 1a72b3da2baf

"""

# revision identifiers, used by Alembic.
revision = 'e66504d94e2e'
down_revision = '1a72b3da2baf'

from alembic import op
from sqlalchemy import sql, func


staticsip = sql.table('staticsip',
                      sql.column('var_name'),
                      sql.column('var_val'))


def upgrade():
    query = (staticsip
             .update()
             .values(var_val='Wazo PBX')
             .where(sql.and_(
                 staticsip.c.var_name == "useragent",
                 func.lower(staticsip.c.var_val) == "xivo pbx")))
    op.execute(query)


def downgrade():
    query = (staticsip
             .update()
             .values(var_val='XiVO PBX')
             .where(sql.and_(
                 staticsip.c.var_name == "useragent",
                 func.lower(staticsip.c.var_val) == "wazo pbx")))
    op.execute(query)
