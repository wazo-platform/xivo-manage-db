"""add_missing_features_func_key

Revision ID: 1a25b8b93e70
Revises: 29013d7926e6

"""

from alembic import op
from sqlalchemy import sql

# revision identifiers, used by Alembic.
revision = '1a25b8b93e70'
down_revision = '29013d7926e6'

FEATURES_DESTINATION_NAME = 'features'
AUTOMON_FUNC_KEY_TYPE = 'dtmf'
AUTOMON_TYPE = 'automon'

features_table = sql.table('features',
                           sql.column('id'),
                           sql.column('category'),
                           sql.column('var_name'))

func_key_table = sql.table('func_key',
                           sql.column('id'),
                           sql.column('type_id'),
                           sql.column('destination_type_id'))

func_key_type_table = sql.table('func_key_type',
                                sql.column('id'),
                                sql.column('name'))

func_key_destination_type_table = sql.table('func_key_destination_type',
                                            sql.column('id'),
                                            sql.column('name'))

func_key_dest_features_table = sql.table('func_key_dest_features',
                                         sql.column('func_key_id'),
                                         sql.column('destination_type_id'),
                                         sql.column('features_id'))


def upgrade():
    features_id = find_features_id()
    query = (
        sql.select([
            sql.func.count(func_key_dest_features_table.c.func_key_id)])
        .where(
            func_key_dest_features_table.c.features_id == features_id))

    count = op.get_bind().execute(query).scalar()

    if count == 0:
        insert_automon_dest_features(find_func_key_type_id(),
                                     find_destination_type_id())


def downgrade():
    pass


def find_func_key_type_id():
    query = (sql.select([func_key_type_table.c.id])
             .where(func_key_type_table.c.name == AUTOMON_FUNC_KEY_TYPE))

    return op.get_bind().execute(query).scalar()


def find_destination_type_id():
    query = (sql.select([func_key_destination_type_table.c.id])
             .where(func_key_destination_type_table.c.name == FEATURES_DESTINATION_NAME))

    return op.get_bind().execute(query).scalar()


def find_features_id():
    features_query = (
        sql.select(
            [features_table.c.id])
        .where(
            sql.and_(
                features_table.c.category == 'featuremap',
                features_table.c.var_name == 'automon')))

    return op.get_bind().execute(features_query).scalar()


def insert_automon_dest_features(type_id, destination_type_id):
    func_key_query = (func_key_table
                      .insert()
                      .returning(func_key_table.c.id)
                      .values(type_id=type_id,
                              destination_type_id=destination_type_id))

    func_key_id = op.get_bind().execute(func_key_query).scalar()

    dest_query = (func_key_dest_features_table
                  .insert()
                  .returning(func_key_dest_features_table.c.func_key_id)
                  .values(func_key_id=func_key_id,
                          destination_type_id=destination_type_id,
                          features_id=find_features_id()))

    return op.get_bind().execute(dest_query).scalar()
