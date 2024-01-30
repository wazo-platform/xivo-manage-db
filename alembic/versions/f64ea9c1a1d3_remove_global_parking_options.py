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
func_key_tbl = sa.sql.table(
    'func_key',
    sa.sql.column('id'),
    sa.sql.column('destination_type_id'),
)
func_key_mapping_tbl = sa.sql.table(
    'func_key_mapping',
    sa.sql.column('func_key_id'),
)
func_key_destination_type_tbl = sa.sql.table(
    'func_key_destination_type',
    sa.sql.column('id'),
    sa.sql.column('name'),
)
func_key_dest_features_tbl = sa.sql.table(
    'func_key_dest_features',
    sa.sql.column('features_id'),
    sa.sql.column('func_key_id'),
)
func_key_dest_park_position_tbl = sa.sql.table(
    'func_key_dest_park_position',
    sa.sql.column('func_key_id'),
)


def upgrade():
    parking_features_subquery = sa.sql.select([features_tbl.c.id]).where(
        sa.and_(
            features_tbl.c.filename == 'features.conf',
            features_tbl.c.category == 'general',
            features_tbl.c.var_name.in_(PARKING_OPTIONS),
        )
    )
    parking_func_key_subquery = sa.sql.select(
        [func_key_dest_features_tbl.c.func_key_id]
    ).where(func_key_dest_features_tbl.c.features_id.in_(parking_features_subquery))
    unpark_func_key_subquery = sa.sql.select(
        [func_key_dest_park_position_tbl.c.func_key_id]
    )

    query = sa.sql.select([func_key_destination_type_tbl.c.id]).where(
        func_key_destination_type_tbl.c.name == 'features'
    )
    destination_type_feature_id = op.get_bind().execute(query).scalar()

    query = sa.sql.select([func_key_destination_type_tbl.c.id]).where(
        func_key_destination_type_tbl.c.name == 'park_position'
    )
    destination_type_park_position_id = op.get_bind().execute(query).scalar()

    # delete existing funckey mapping to park to global parking
    query = func_key_mapping_tbl.delete().where(
        func_key_mapping_tbl.c.func_key_id.in_(parking_func_key_subquery)
    )
    op.execute(query)
    # delete existing dest funckeys to park to global parking
    query = func_key_dest_features_tbl.delete().where(
        func_key_dest_features_tbl.c.features_id.in_(parking_features_subquery)
    )
    op.execute(query)
    # delete existing funckeys to park to global parking
    linked_funckey_subquery = sa.sql.select([func_key_dest_features_tbl.c.func_key_id])
    query = func_key_tbl.delete().where(
        sa.and_(
            func_key_tbl.c.destination_type_id == destination_type_feature_id,
            sa.sql.not_(func_key_tbl.c.id.in_(linked_funckey_subquery)),
        )
    )
    op.execute(query)

    # delete existing funckey mapping to unpark
    query = func_key_mapping_tbl.delete().where(
        func_key_mapping_tbl.c.func_key_id.in_(unpark_func_key_subquery)
    )
    op.execute(query)
    # delete all unpark funckeys, as they all point to the global parking
    query = func_key_dest_park_position_tbl.delete()
    op.execute(query)
    # delete existing funckeys to unpark
    query = func_key_tbl.delete().where(
        func_key_tbl.c.destination_type_id == destination_type_park_position_id
    )
    op.execute(query)

    # delete features options
    query = features_tbl.delete().where(
        features_tbl.c.id.in_(parking_features_subquery)
    )
    op.execute(query)


def downgrade():
    pass
