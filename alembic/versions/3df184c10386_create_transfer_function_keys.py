"""create transfer function keys

Revision ID: 3df184c10386
Revises: 234745874c55

"""

# revision identifiers, used by Alembic.
revision = '3df184c10386'
down_revision = '234745874c55'

from alembic import op
import sqlalchemy as sa


DTMF_TYPE_NAME = 'dtmf'
FEATURES_TYPE_NAME = 'features'

BLIND_TRANSFER_TYPE = 'blindxfer'
ATTENDED_TRANSFER_TYPE = 'atxfer'

func_key_table = sa.sql.table('func_key',
                              sa.sql.column('id'),
                              sa.sql.column('type_id'),
                              sa.sql.column('destination_type_id'))

func_key_type_table = sa.sql.table('func_key_type',
                                   sa.sql.column('id'),
                                   sa.sql.column('name'))

func_key_destination_type_table = sa.sql.table('func_key_destination_type',
                                               sa.sql.column('id'),
                                               sa.sql.column('name'))

func_key_dest_features_table = sa.sql.table('func_key_dest_features',
                                            sa.sql.column('func_key_id'),
                                            sa.sql.column('destination_type_id'),
                                            sa.sql.column('features_id'))

features_table = sa.sql.table('features',
                              sa.sql.column('id'),
                              sa.sql.column('category'),
                              sa.sql.column('var_name'))


def upgrade():
    type_id = insert_dtmf_type()
    destination_type_id = find_features_type()
    insert_transfer_func_key(type_id, destination_type_id, BLIND_TRANSFER_TYPE)
    insert_transfer_func_key(type_id, destination_type_id, ATTENDED_TRANSFER_TYPE)


def insert_dtmf_type():
    query = (func_key_type_table
             .insert()
             .returning(func_key_type_table.c.id)
             .values(name=DTMF_TYPE_NAME))

    return op.get_bind().execute(query).scalar()


def find_features_type():
    query = (sa.sql.select([func_key_destination_type_table.c.id])
             .where(func_key_destination_type_table.c.name == FEATURES_TYPE_NAME))

    return op.get_bind().execute(query).scalar()


def insert_transfer_func_key(type_id, destination_type_id, transfer_type):
    func_key_query = (func_key_table
                      .insert()
                      .returning(func_key_table.c.id)
                      .values(type_id=type_id,
                              destination_type_id=destination_type_id))

    func_key_id = op.get_bind().execute(func_key_query).scalar()

    features_query = (
        sa.sql.select(
            [features_table.c.id])
        .where(
            sa.sql.and_(
                features_table.c.category == 'featuremap',
                features_table.c.var_name == transfer_type)))

    features_id = op.get_bind().execute(features_query).scalar()

    dest_query = (func_key_dest_features_table
                  .insert()
                  .returning(func_key_dest_features_table.c.func_key_id)
                  .values(func_key_id=func_key_id,
                          destination_type_id=destination_type_id,
                          features_id=features_id))

    return op.get_bind().execute(dest_query).scalar()


def downgrade():
    features_query = (sa.sql.select([features_table.c.id])
                      .where(
                          sa.sql.and_(
                              features_table.c.category == 'featuremap',
                              features_table.c.var_name.in_((BLIND_TRANSFER_TYPE,
                                                            ATTENDED_TRANSFER_TYPE))))
                      .alias())

    query = (sa.sql.select([func_key_dest_features_table.c.func_key_id])
             .where(
                 func_key_dest_features_table.c.features_id.in_(features_query))
             )

    for row in op.get_bind().execute(query):
        dest_query = (func_key_dest_features_table
                      .delete()
                      .where(func_key_dest_features_table.c.func_key_id == row.func_key_id))

        func_key_query = (func_key_table
                          .delete()
                          .where(func_key_table.c.id == row.func_key_id))

        op.get_bind().execute(dest_query)
        op.get_bind().execute(func_key_query)

    op.execute(func_key_type_table
               .delete()
               .where(func_key_type_table.c.name == DTMF_TYPE_NAME))
