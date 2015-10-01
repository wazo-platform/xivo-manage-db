"""use automixmon features instead of automixmon

Revision ID: 500ca962c3a8
Revises: 2ea8d6cb26f6

"""

# revision identifiers, used by Alembic.
revision = '500ca962c3a8'
down_revision = '2ea8d6cb26f6'

from alembic import op
from sqlalchemy import sql, and_

features_table = sql.table('features',
                           sql.column('category'),
                           sql.column('var_name'))


def upgrade():
    op.execute(features_table
               .update()
               .where(and_(features_table.c.category == 'featuremap',
                           features_table.c.var_name == 'automon'))
               .values(var_name='automixmon'))


def downgrade():
    op.execute(features_table
               .update()
               .where(and_(features_table.c.category == 'featuremap',
                           features_table.c.var_name == 'automixmon'))
               .values(var_name='automon'))
