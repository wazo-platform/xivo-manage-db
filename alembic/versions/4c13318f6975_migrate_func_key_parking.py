"""migrate func key parking

Revision ID: 4c13318f6975
Revises: a3e7fd7b670
XiVO Version: <version>

"""

# revision identifiers, used by Alembic.
revision = '4c13318f6975'
down_revision = 'a3e7fd7b670'

from alembic import op
import sqlalchemy as sa
from sqlalchemy import sql


TYPE_SPEEDDIAL = 'speeddial'

DESTINATION_PARKING_ID = 7
DESTINATION_PARKING_NAME = 'parking'

PARKING_TYPE = 'parkpos'


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

destination_parking_table = sql.table('func_key_dest_parking',
                                      sql.column('func_key_id'),
                                      sql.column('destination_type_id'),
                                      sql.column('park_position'))

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


func_key_columns = (
    phonefunckey_table.c.iduserfeatures.label('user_id'),
    phonefunckey_table.c.fknum.label('position'),
    phonefunckey_table.c.label,
    phonefunckey_table.c.exten.label('park_position'),
    sql.cast(phonefunckey_table.c.supervision, sa.Boolean).label('blf'),
)

old_func_key_columns = (
    func_key_mapping_table.c.func_key_id,
    func_key_mapping_table.c.template_id,
    func_key_mapping_table.c.position,
    func_key_mapping_table.c.blf,
    func_key_mapping_table.c.label,
    destination_parking_table.c.park_position,
    user_table.c.id.label('user_id')
)

func_keys_query = (sql.select(func_key_columns)
                   .where(phonefunckey_table.c.typevalextenumbers == PARKING_TYPE))


old_func_keys_query = (sql.select(old_func_key_columns,
                                  from_obj=[
                                      func_key_mapping_table.join(
                                          destination_parking_table,
                                          func_key_mapping_table.c.func_key_id == destination_parking_table.c.func_key_id)
                                      .join(template_table,
                                            func_key_mapping_table.c.template_id == template_table.c.id)
                                      .join(user_table,
                                            template_table.c.id == user_table.c.func_key_private_template_id)
                                  ]))


def upgrade():
    delete_duplicate_fks()
    migrate_func_keys()
    delete_old_func_keys()


def delete_duplicate_fks():
    for row in get_duplicate_func_keys():
        delete_duplicate_fk(row.iduserfeatures, row.exten, row.fknum)


def get_duplicate_func_keys():
    columns = (phonefunckey_table.c.iduserfeatures,
               phonefunckey_table.c.exten,
               sa.func.min(phonefunckey_table.c.fknum).label("first_position"))

    valid_fk_subq = (sql.select(columns)
                     .where(
                         phonefunckey_table.c.typevalextenumbers == PARKING_TYPE)
                     .group_by(
                         phonefunckey_table.c.iduserfeatures,
                         phonefunckey_table.c.exten)
                     .having(
                         sa.func.count(phonefunckey_table.c.exten) > 1)
                     .alias())

    columns = (phonefunckey_table.c.iduserfeatures,
               phonefunckey_table.c.exten,
               phonefunckey_table.c.fknum)

    join_condition = sql.and_(
        phonefunckey_table.c.exten == valid_fk_subq.c.exten,
        phonefunckey_table.c.fknum > valid_fk_subq.c.first_position,
        phonefunckey_table.c.iduserfeatures == valid_fk_subq.c.iduserfeatures)

    duplicate_fk_query = (sql.select(columns,
                                     from_obj=[
                                         phonefunckey_table.join(
                                             valid_fk_subq,
                                             join_condition
                                         )
                                     ]))

    return op.get_bind().execute(duplicate_fk_query)


def delete_duplicate_fk(iduserfeatures, exten, fknum):
    print('[MIGRATE_FK] : Deleting func key for user "%s" (fk position %s with park position %s)' %
          (iduserfeatures, fknum, exten))

    query = (phonefunckey_table
             .delete()
             .where(sql.and_(
                 phonefunckey_table.c.iduserfeatures == iduserfeatures,
                 phonefunckey_table.c.exten == exten,
                 phonefunckey_table.c.fknum == fknum)))

    op.get_bind().execute(query)


def migrate_func_keys():
    for row in op.get_bind().execute(func_keys_query):
        func_key_id = create_func_key()
        create_parking_destination(func_key_id, row.park_position)
        create_mapping(func_key_id, row)


def create_func_key():
    speeddial_id = get_speeddial_id()
    insert_query = (func_key_table
                    .insert()
                    .returning(func_key_table.c.id)
                    .values(type_id=speeddial_id,
                            destination_type_id=DESTINATION_PARKING_ID))

    return op.get_bind().execute(insert_query).scalar()


def get_speeddial_id():
    return op.get_bind().execute(
        sql.select(
            [func_key_type_table.c.id])
        .where(
            func_key_type_table.c.name == TYPE_SPEEDDIAL)
    ).scalar()


def create_parking_destination(func_key_id, park_position):
    destination_query = (destination_parking_table
                         .insert()
                         .returning(destination_parking_table.c.func_key_id)
                         .values(func_key_id=func_key_id,
                                 park_position=park_position))

    op.get_bind().execute(destination_query)


def create_mapping(func_key_id, func_key_row):
    conn = op.get_bind()

    template_id = conn.execute(sql.select(
        [user_table.c.func_key_private_template_id])
        .where(
            user_table.c.id == func_key_row.user_id)
    ).scalar()

    mapping_query = (func_key_mapping_table
                     .insert()
                     .returning(func_key_mapping_table.c.func_key_id)
                     .values(func_key_id=func_key_id,
                             template_id=template_id,
                             destination_type_id=DESTINATION_PARKING_ID,
                             label=func_key_row.label,
                             position=func_key_row.position,
                             blf=func_key_row.blf))

    conn.execute(mapping_query)


def delete_old_func_keys():
    delete_query = (phonefunckey_table
                    .delete()
                    .where(phonefunckey_table.c.typevalextenumbers == PARKING_TYPE))

    op.get_bind().execute(delete_query)


def downgrade():
    for row in op.get_bind().execute(old_func_keys_query):
        create_old_func_keys(row)
        delete_mapping(row.func_key_id, row.template_id)
        delete_dest_parking(row.func_key_id)
        delete_func_key(row.func_key_id)


def create_old_func_keys(row):
    supervision = 1 if row.blf else 0

    row = {'iduserfeatures': row.user_id,
           'fknum': row.position,
           'typeextenumbers': 'generalfeatures',
           'typevalextenumbers': 'parkpos',
           'typeextenumbersright': None,
           'typevalextenumbersright': None,
           'label': row.label,
           'exten': row.park_position,
           'supervision': supervision}

    op.bulk_insert(phonefunckey_table, [row])


def delete_mapping(func_key_id, template_id):
    query = (func_key_mapping_table
             .delete()
             .where(sql.and_(
                 func_key_mapping_table.c.func_key_id == func_key_id,
                 func_key_mapping_table.c.template_id == template_id)))

    op.get_bind().execute(query)


def delete_dest_parking(func_key_id):
    query = (destination_parking_table
             .delete())

    op.get_bind().execute(query)


def delete_func_key(func_key_id):
    query = (func_key_table
             .delete()
             .where(func_key_table.c.destination_type_id == DESTINATION_PARKING_ID))

    op.get_bind().execute(query)
