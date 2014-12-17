"""create_automon_func_key

Revision ID: 35a7f7e2dc33
Revises: 3ab28f25de30

"""

# revision identifiers, used by Alembic.
revision = '35a7f7e2dc33'
down_revision = '3ab28f25de30'

from alembic import op
from sqlalchemy import sql
import sqlalchemy as sa


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

func_key_mapping_table = sql.table('func_key_mapping',
                                   sql.column('template_id'),
                                   sql.column('func_key_id'),
                                   sql.column('destination_type_id'),
                                   sql.column('label'),
                                   sql.column('position'),
                                   sql.column('blf'))

phonefunckey_table = sql.table('phonefunckey',
                               sql.column('iduserfeatures'),
                               sql.column('fknum'),
                               sql.column('exten'),
                               sql.column('typeextenumbers'),
                               sql.column('typevalextenumbers'),
                               sql.column('typeextenumbersright'),
                               sql.column('typevalextenumbersright'),
                               sql.column('label'),
                               sql.column('supervision'),
                               sql.column('progfunckey'))

user_table = sql.table('userfeatures',
                       sql.column('id'),
                       sql.column('func_key_private_template_id'))


func_key_columns = (
    phonefunckey_table.c.iduserfeatures.label('user_id'),
    phonefunckey_table.c.fknum.label('position'),
    phonefunckey_table.c.label,
    phonefunckey_table.c.exten.label('park_position'),
    sql.cast(phonefunckey_table.c.supervision, sa.Boolean).label('blf'),
)

func_keys_query = (sql.select(func_key_columns)
                   .where(phonefunckey_table.c.typevalextenumbers == AUTOMON_TYPE))


def upgrade():
    type_id = find_func_key_type_id()
    destination_type_id = find_destination_type_id()
    func_key_id = insert_automon_dest_features(type_id, destination_type_id)
    migrate_func_keys(func_key_id, destination_type_id)
    delete_old_func_keys()


def downgrade():
    op.execute(func_key_dest_features_table
               .delete()
               .where(func_key_dest_features_table.c.features_id == find_features_id()))


def migrate_func_keys(func_key_id, destination_type_id):
    for row in op.get_bind().execute(func_keys_query):
        create_mapping(func_key_id, row, destination_type_id)


def create_mapping(func_key_id, func_key_row, destination_type_id):
    conn = op.get_bind()

    template_query = (
        sql.select(
            [user_table.c.func_key_private_template_id])
        .where(
            user_table.c.id == func_key_row.user_id))

    template_id = conn.execute(template_query).scalar()

    mapping_query = (func_key_mapping_table
                     .insert()
                     .returning(func_key_mapping_table.c.func_key_id)
                     .values(func_key_id=func_key_id,
                             template_id=template_id,
                             destination_type_id=destination_type_id,
                             label=func_key_row.label,
                             position=func_key_row.position,
                             blf=func_key_row.blf))

    conn.execute(mapping_query)


def delete_old_func_keys():
    delete_query = (phonefunckey_table
                    .delete()
                    .where(phonefunckey_table.c.typevalextenumbers == AUTOMON_TYPE))

    op.get_bind().execute(delete_query)


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
