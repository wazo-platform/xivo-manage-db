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
                           sql.column('var_name'),
                           sql.column('commented'))


def upgrade():
    _remove_features((
        'pickupsound',
        'pickupfailsound',
    ))
    _uncomment_features((
        'parkinghints',
        'parkingtime',
        'comebacktoorigin',
        'parkedplay',
        'parkedcalltransfers',
        'parkedcallreparking',
        'parkedcallhangup',
        'parkedcallrecording',
        'parkeddynamic',
        'adsipark',
        'findslot',
        'parkedmusicclass',
        'transferdigittimeout',
        'pickupexten',
        'pickupsound',
        'pickupfailsound',
        'featuredigittimeout',
        'atxfernoanswertimeout',
        'atxferdropcall',
        'atxferloopdelay',
        'atxfercallbackretries',
    ))


def _uncomment_features(feature_names):
    op.execute(features_table
               .update()
               .where(features_table.c.var_name.in_(feature_names))
               .values({'commented': 0}))


def _remove_features(feature_names):
    delete_query = (features_table
                    .delete()
                    .where(features_table.c.var_name.in_(feature_names)))

    op.get_bind().execute(delete_query)


def downgrade():
    pass
