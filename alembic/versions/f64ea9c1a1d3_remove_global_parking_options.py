"""remove global parking options

Revision ID: f64ea9c1a1d3
Revises: 091acfe39b68

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f64ea9c1a1d3'
down_revision = '091acfe39b68'

PARKING_OPTIONS = [
    'comebacktoorigin',
    'context',
    'courtesytone',
    'findslot',
    'parkedcallhangup',
    'parkedcallrecording',
    'parkedcallreparking',
    'parkedcalltransfers',
    'parkeddynamic',
    'parkedmusicclass',
    'parkedplay',
    'parkext',
    'parkinghints',
    'parkingtime',
    'parkpos',
]

features_tbl = sa.sql.table(
    'features',
    sa.sql.column('id'),
    sa.sql.column('filename'),
    sa.sql.column('category'),
    sa.sql.column('var_name'),
)
func_key_dest_features_tbl = sa.sql.table(
    'func_key_dest_features',
    sa.sql.column('features_id'),
)
func_key_dest_park_position_tbl = sa.sql.table(
    'func_key_dest_park_position',
)


def upgrade():
    parking_features_subquery = sa.sql.select([features_tbl.c.id]).where(
        sa.and_(
            features_tbl.c.filename == 'features.conf',
            features_tbl.c.category == 'general',
            features_tbl.c.var_name.in_(PARKING_OPTIONS),
        )
    )
    # delete existing funckeys to park to global parking
    query = func_key_dest_features_tbl.delete().where(
        func_key_dest_features_tbl.c.features_id.in_(parking_features_subquery)
    )
    op.execute(query)
    # delete all unpark funckeys, as they all point to the global parking
    query = func_key_dest_park_position_tbl.delete()
    op.execute(query)
    # delete features options
    query = features_tbl.delete().where(
        features_tbl.c.id.in_(parking_features_subquery)
    )
    op.execute(query)


def downgrade():
    pass
