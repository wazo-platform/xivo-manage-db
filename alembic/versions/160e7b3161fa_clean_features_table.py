"""clean features table

Revision ID: 160e7b3161fa
Revises: 45ceb32fae06

"""

# revision identifiers, used by Alembic.
revision = '160e7b3161fa'
down_revision = '45ceb32fae06'

from alembic import op
from sqlalchemy import sql


features_table = sql.table('features',
                           sql.column('var_name'))


def upgrade():
    _remove_features(('pickupsound', 'pickupfailsound'))


def _remove_features(feature_names):
    delete_query = (features_table
                    .delete()
                    .where(features_table.c.var_name.in_(feature_names)))

    op.get_bind().execute(delete_query)


def downgrade():
    pass
