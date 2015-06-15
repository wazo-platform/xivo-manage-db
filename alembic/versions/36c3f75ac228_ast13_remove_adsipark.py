"""ast13: remove adsipark

Revision ID: 36c3f75ac228
Revises: f5f2dd21819

"""

# revision identifiers, used by Alembic.
revision = '36c3f75ac228'
down_revision = 'f5f2dd21819'

from alembic import op
from sqlalchemy import sql


features_table = sql.table('features',
                           sql.column('var_name'))


def upgrade():
    _delete_features_adsipark()


def _delete_features_adsipark():
    op.execute(features_table.delete().where(features_table.c.var_name == 'adsipark'))


def downgrade():
    pass
