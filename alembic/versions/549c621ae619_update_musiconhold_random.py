"""update musiconhold random

Revision ID: 549c621ae619
Revises: 544f8b1e6905

"""

# revision identifiers, used by Alembic.
revision = '549c621ae619'
down_revision = '544f8b1e6905'

from alembic import op
from sqlalchemy import sql

musiconhold = sql.table('musiconhold',
                        sql.column('var_name'),
                        sql.column('var_val'))


def upgrade():
    op.execute(musiconhold.update()
               .where(musiconhold.c.var_name == 'random')
               .values(
                   var_name='sort',
                   var_val=sql.case([(musiconhold.c.var_val == 'yes', 'random')])))


def downgrade():
    op.execute(musiconhold.update()
               .where(musiconhold.c.var_name == 'sort')
               .values(
                   var_name='random',
                   var_val=sql.case([(musiconhold.c.var_val == 'random', 'yes')], else_='no')))
