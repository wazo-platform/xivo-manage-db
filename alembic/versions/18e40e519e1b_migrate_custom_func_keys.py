"""migrate custom func keys

Revision ID: 18e40e519e1b
Revises: 3fe6319ce27a

"""

# revision identifiers, used by Alembic.
revision = '18e40e519e1b'
down_revision = '3fe6319ce27a'

from alembic import op
import sqlalchemy as sa
from sqlalchemy import sql


TYPE_SPEEDDIAL = 'speeddial'

DESTINATION_CUSTOM_ID = 10


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

func_key_type_table = sql.table('func_key_type',
                                sql.column('id'),
                                sql.column('name'))

destination_type_table = sql.table('func_key_destination_type',
                                   sql.column('id'),
                                   sql.column('name'))

func_key_mapping_table = sql.table('func_key_mapping',
                                   sql.column('template_id'),
                                   sql.column('func_key_id'),
                                   sql.column('destination_type_id'),
                                   sql.column('label'),
                                   sql.column('position'),
                                   sql.column('blf'))

dest_custom_table = sql.table('func_key_dest_custom',
                              sql.column('func_key_id'),
                              sql.column('destination_type_id'),
                              sql.column('exten'))

template_table = sql.table('func_key_template', sql.column('id'))

user_table = sql.table('userfeatures',
                       sql.column('id'),
                       sql.column('func_key_private_template_id'))


func_key_columns = (
    phonefunckey_table.c.iduserfeatures.label('user_id'),
    phonefunckey_table.c.fknum.label('position'),
    phonefunckey_table.c.label,
    sql.cast(phonefunckey_table.c.supervision, sa.Boolean).label('blf'),
    phonefunckey_table.c.exten.label('exten')
)

old_func_key_columns = (
    func_key_mapping_table.c.func_key_id,
    func_key_mapping_table.c.template_id,
    func_key_mapping_table.c.position,
    func_key_mapping_table.c.blf,
    func_key_mapping_table.c.label,
    dest_custom_table.c.exten,
    user_table.c.id.label('user_id')
)


func_keys_query = (sql.select(func_key_columns)
                   .where(
                       sql.and_(
                           phonefunckey_table.c.typevalextenumbers == None,
                           phonefunckey_table.c.typevalextenumbersright == None,
                           phonefunckey_table.c.typeextenumbersright == None,
                           phonefunckey_table.c.typevalextenumbersright == None))
                   )


old_func_keys_query = (sql.select(old_func_key_columns,
                                  from_obj=[
                                      func_key_mapping_table.join(
                                          dest_custom_table,
                                          func_key_mapping_table.c.func_key_id == dest_custom_table.c.func_key_id)
                                      .join(template_table,
                                            func_key_mapping_table.c.template_id == template_table.c.id)
                                      .join(user_table,
                                            template_table.c.id == user_table.c.func_key_private_template_id)
                                  ]))


def upgrade():
    delete_invalid_user_func_keys()
    delete_empty_customs()
    migrate_func_keys()
    delete_old_func_keys()


def delete_invalid_user_func_keys():
    query = (phonefunckey_table
             .delete()
             .where(
                 ~phonefunckey_table.c.iduserfeatures.in_(sql.select([user_table.c.id])))
             )

    op.get_bind().execute(query)


def delete_empty_customs():
    template = '[MIGRATE_FK] : Deleting func key for user "%s" (fk position %s with empty custom)'

    columns = (phonefunckey_table.c.iduserfeatures,
               phonefunckey_table.c.fknum)

    query = (sql.select(columns)
             .where(
                 sql.and_(
                     phonefunckey_table.c.typevalextenumbers == None,
                     phonefunckey_table.c.typevalextenumbersright == None,
                     phonefunckey_table.c.typeextenumbersright == None,
                     phonefunckey_table.c.typevalextenumbersright == None,
                     sql.or_(
                         phonefunckey_table.c.exten == None,
                         phonefunckey_table.c.exten == '')))
             )

    for row in op.get_bind().execute(query):
        message = template % (row.iduserfeatures, row.fknum)
        delete_fk(row, message)


def delete_fk(row, message):
    print(message)

    query = (phonefunckey_table
             .delete()
             .where(
                 sql.and_(
                     phonefunckey_table.c.iduserfeatures == row.iduserfeatures,
                     phonefunckey_table.c.fknum == row.fknum))
             )

    op.get_bind().execute(query)


def migrate_func_keys():
    for row in op.get_bind().execute(func_keys_query):
        func_key_id = create_func_key()
        create_custom_destination(func_key_id, row.exten)
        create_mapping(func_key_id, row)


def create_func_key():
    speeddial_id = get_speeddial_id()
    insert_query = (func_key_table
                    .insert()
                    .returning(func_key_table.c.id)
                    .values(type_id=speeddial_id,
                            destination_type_id=DESTINATION_CUSTOM_ID))

    return op.get_bind().execute(insert_query).scalar()


def get_speeddial_id():
    return op.get_bind().execute(
        sql.select(
            [func_key_type_table.c.id])
        .where(
            func_key_type_table.c.name == TYPE_SPEEDDIAL)
    ).scalar()


def create_custom_destination(func_key_id, exten):
    destination_query = (dest_custom_table
                         .insert()
                         .returning(dest_custom_table.c.func_key_id)
                         .values(func_key_id=func_key_id,
                                 exten=exten))

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
                             destination_type_id=DESTINATION_CUSTOM_ID,
                             label=func_key_row.label,
                             position=func_key_row.position,
                             blf=func_key_row.blf))

    conn.execute(mapping_query)


def delete_old_func_keys():
    delete_query = (phonefunckey_table
                    .delete()
                    .where(
                        sql.and_(
                            phonefunckey_table.c.typevalextenumbers == None,
                            phonefunckey_table.c.typevalextenumbersright == None,
                            phonefunckey_table.c.typeextenumbersright == None,
                            phonefunckey_table.c.typevalextenumbersright == None))
                    )

    op.get_bind().execute(delete_query)


def downgrade():
    for row in op.get_bind().execute(old_func_keys_query):
        create_old_func_keys(row)
        delete_mapping(row.func_key_id, row.template_id)
        delete_dest_custom(row.func_key_id)
        delete_func_key(row.func_key_id)


def create_old_func_keys(row):
    supervision = 1 if row.blf else 0

    row = {'iduserfeatures': row.user_id,
           'fknum': row.position,
           'typeextenumbers': None,
           'typevalextenumbers': None,
           'typeextenumbersright': None,
           'typevalextenumbersright': None,
           'label': row.label,
           'exten': row.exten,
           'supervision': supervision}

    op.bulk_insert(phonefunckey_table, [row])


def delete_mapping(func_key_id, template_id):
    query = (func_key_mapping_table
             .delete()
             .where(sql.and_(
                 func_key_mapping_table.c.func_key_id == func_key_id,
                 func_key_mapping_table.c.template_id == template_id)))

    op.get_bind().execute(query)


def delete_dest_custom(func_key_id):
    query = (dest_custom_table
             .delete())

    op.get_bind().execute(query)


def delete_func_key(func_key_id):
    query = (func_key_table
             .delete()
             .where(func_key_table.c.destination_type_id == DESTINATION_CUSTOM_ID))

    op.get_bind().execute(query)
