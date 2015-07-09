"""ast13: update findslot

Revision ID: 501dae22d6be
Revises: 36c3f75ac228

"""

# revision identifiers, used by Alembic.
revision = '501dae22d6be'
down_revision = '36c3f75ac228'

from alembic import op
from sqlalchemy import sql


features_table = sql.table('features',
                           sql.column('var_name'),
                           sql.column('var_val'))


def upgrade():
    _update_features_findslot()


def _update_features_findslot():
    op.execute(features_table.update().
               where(sql.and_(
                   features_table.c.var_name == 'findslot',
                   features_table.c.var_val == 'no')).
               values(var_val='first'))


def downgrade():
    pass
