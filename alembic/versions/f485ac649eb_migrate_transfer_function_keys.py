"""migrate transfer function keys

Revision ID: f485ac649eb
Revises: 3df184c10386

"""

# revision identifiers, used by Alembic.
revision = 'f485ac649eb'
down_revision = '3df184c10386'

from alembic import op
import sqlalchemy as sa
from sqlalchemy import sql

FEATURE_MAP_TYPE = 'featuremap'


BLIND_TRANSFER_TYPE = 'blindxfer'
ATTENDED_TRANSFER_TYPE = 'atxfer'

DESTINATION_FEATURES_ID = 8

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

func_key_table = sql.table('func_key',
                           sql.column('id'),
                           sql.column('type_id'),
                           sql.column('destination_type_id'))

dest_features_table = sql.table('func_key_dest_features',
                                sql.column('func_key_id'),
                                sql.column('destination_type_id'),
                                sql.column('features_id'))

func_key_type_table = sql.table('func_key_type',
                                sql.column('id'),
                                sql.column('name'))

func_key_mapping_table = sql.table('func_key_mapping',
                                   sql.column('template_id'),
                                   sql.column('func_key_id'),
                                   sql.column('destination_type_id'),
                                   sql.column('label'),
                                   sql.column('position'),
                                   sql.column('blf'))

template_table = sql.table('func_key_template', sql.column('id'))

user_table = sql.table('userfeatures',
                       sql.column('id'),
                       sql.column('func_key_private_template_id'))

destination_type_table = sql.table('func_key_destination_type',
                                   sql.column('id'),
                                   sql.column('name'))

features_table = sql.table('features',
                           sql.column('id'),
                           sql.column('category'),
                           sql.column('var_name'))


def upgrade():
    delete_duplicate_fks()
    migrate_func_keys()
    delete_old_func_keys()


def delete_duplicate_fks():
    for row in get_duplicate_func_keys():
        delete_duplicate_fk(row.iduserfeatures, row.fknum)


def get_duplicate_func_keys():
    transfer_types = (BLIND_TRANSFER_TYPE, ATTENDED_TRANSFER_TYPE)

    columns = (phonefunckey_table.c.iduserfeatures,
               phonefunckey_table.c.typevalextenumbers,
               sa.func.min(phonefunckey_table.c.fknum).label("first_position"))

    duplicate_query = (sql.select(columns)
                       .where(
                           phonefunckey_table.c.typevalextenumbers.in_(transfer_types))
                       .group_by(
                           phonefunckey_table.c.typevalextenumbers,
                           phonefunckey_table.c.iduserfeatures)
                       .having(
                           sa.func.count(phonefunckey_table.c.typevalextenumbers) > 1)
                       .alias())

    columns = (phonefunckey_table.c.iduserfeatures,
               phonefunckey_table.c.fknum)

    join_condition = phonefunckey_table.join(
        duplicate_query,
        sql.and_(
            phonefunckey_table.c.typevalextenumbers == duplicate_query.c.typevalextenumbers,
            phonefunckey_table.c.fknum > duplicate_query.c.first_position,
            phonefunckey_table.c.iduserfeatures == duplicate_query.c.iduserfeatures))

    duplicate_fk_query = sql.select(columns, from_obj=[join_condition])

    return op.get_bind().execute(duplicate_fk_query)


def delete_duplicate_fk(iduserfeatures, fknum):
    print('[MIGRATE_FK] : Deleting transfer func key for user "%s" (fk position %s)' %
          (iduserfeatures, fknum))

    query = (phonefunckey_table
             .delete()
             .where(sql.and_(
                 phonefunckey_table.c.iduserfeatures == iduserfeatures,
                 phonefunckey_table.c.fknum == fknum)))

    op.get_bind().execute(query)


def migrate_func_keys():
    for row in get_func_keys():
        func_key_id = get_transfer_func_key(row.transfer_type)
        create_mapping(func_key_id, row)


def get_func_keys():
    columns = (
        phonefunckey_table.c.iduserfeatures.label('user_id'),
        phonefunckey_table.c.fknum.label('position'),
        phonefunckey_table.c.label,
        phonefunckey_table.c.typevalextenumbers.label('transfer_type'),
        sql.cast(phonefunckey_table.c.supervision, sa.Boolean).label('blf'),
    )

    query = (sql.select(columns)
             .where(
                 sql.and_(
                     phonefunckey_table.c.typeextenumbers == FEATURE_MAP_TYPE,
                     phonefunckey_table.c.typevalextenumbers.in_((
                         BLIND_TRANSFER_TYPE,
                         ATTENDED_TRANSFER_TYPE))))
             )

    return op.get_bind().execute(query)


def get_transfer_func_key(transfer_type):
    transfer_subquery = (
        sql.select(
            [features_table.c.id])
        .where(
            sql.and_(
                features_table.c.category == 'featuremap',
                features_table.c.var_name == transfer_type))
        .alias())

    query = (
        sql.select(
            [dest_features_table.c.func_key_id])
        .where(
            dest_features_table.c.features_id == transfer_subquery))

    return op.get_bind().execute(query).scalar()


def create_mapping(func_key_id, func_key_row):
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
                             destination_type_id=DESTINATION_FEATURES_ID,
                             label=func_key_row.label,
                             position=func_key_row.position,
                             blf=func_key_row.blf))

    conn.execute(mapping_query)


def delete_old_func_keys():
    delete_query = (phonefunckey_table
                    .delete()
                    .where(
                        phonefunckey_table.c.typevalextenumbers.in_(
                            (BLIND_TRANSFER_TYPE, ATTENDED_TRANSFER_TYPE)))
                    )

    op.get_bind().execute(delete_query)


def downgrade():
    for row in get_old_func_keys():
        create_old_func_keys(row)
        delete_mapping(row.func_key_id, row.template_id)


def get_old_func_keys():
    columns = (
        func_key_mapping_table.c.func_key_id,
        func_key_mapping_table.c.template_id,
        func_key_mapping_table.c.position,
        func_key_mapping_table.c.blf,
        func_key_mapping_table.c.label,
        features_table.c.var_name.label('transfer_type'),
        user_table.c.id.label('user_id')
    )

    join_conditions = (func_key_mapping_table
                       .join(dest_features_table,
                             func_key_mapping_table.c.func_key_id == dest_features_table.c.func_key_id)
                       .join(features_table,
                             dest_features_table.c.features_id == features_table.c.id)
                       .join(template_table,
                             func_key_mapping_table.c.template_id == template_table.c.id)
                       .join(user_table,
                             template_table.c.id == user_table.c.func_key_private_template_id))

    query = (sql.select(columns, from_obj=[join_conditions])
             .where(
                 features_table.c.var_name.in_(
                     (BLIND_TRANSFER_TYPE, ATTENDED_TRANSFER_TYPE)))
             )

    return op.get_bind().execute(query)


def create_old_func_keys(row):
    supervision = 1 if row.blf else 0

    row = {'iduserfeatures': row.user_id,
           'fknum': row.position,
           'typeextenumbers': 'featuremap',
           'typevalextenumbers': row.transfer_type,
           'typeextenumbersright': None,
           'typevalextenumbersright': None,
           'label': row.label,
           'exten': None,
           'supervision': supervision}

    op.bulk_insert(phonefunckey_table, [row])


def delete_mapping(func_key_id, template_id):
    query = (func_key_mapping_table
             .delete()
             .where(sql.and_(
                 func_key_mapping_table.c.func_key_id == func_key_id,
                 func_key_mapping_table.c.template_id == template_id)))

    op.get_bind().execute(query)
