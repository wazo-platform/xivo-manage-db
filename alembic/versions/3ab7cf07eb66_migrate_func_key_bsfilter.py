"""migrate func key bsfilter

Revision ID: 3ab7cf07eb66
Revises: 11b792bcc775

"""

# revision identifiers, used by Alembic.
revision = '3ab7cf07eb66'
down_revision = '11b792bcc775'

from alembic import op
import sqlalchemy as sa
from sqlalchemy import sql

BSFILTER_TYPE = 'bsfilter'
SECRETARY_TYPE = 'secretary'
BOSS_TYPE = 'boss'
TYPE_ID = 1
DESTINATION_TYPE_ID = 12

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

dest_bsfilter_table = sql.table('func_key_dest_bsfilter',
                                sql.column('func_key_id'),
                                sql.column('destination_type_id'),
                                sql.column('filtermember_id'))

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

user_table = sql.table('userfeatures',
                       sql.column('id'),
                       sql.column('func_key_private_template_id'))

template_table = sql.table('func_key_template', sql.column('id'))

destination_type_table = sql.table('func_key_destination_type',
                                   sql.column('id'),
                                   sql.column('name'))

callfilter_table = sql.table('callfilter',
                             sql.column('id'),
                             sql.column('callfilterid'),
                             sql.column('type'),
                             sql.column('typeval'),
                             sql.column('bstype'))

callfiltermember_table = sql.table('callfiltermember',
                                   sql.column('id'),
                                   sql.column('callfilterid'),
                                   sql.column('type'),
                                   sql.column('typeval'),
                                   sql.column('bstype'))


def upgrade():
    delete_bsfilters_without_bosses()
    delete_missing_bsfilter_funckeys()
    delete_duplicate_bsfilter_funckeys()
    create_bsfilter_func_keys()
    migrate_func_keys()
    delete_old_func_keys()


def delete_bsfilters_without_bosses():
    for bsfilter_id in get_bsfilters_without_bosses():
        delete_bsfilter(bsfilter_id)


def get_bsfilters_without_bosses():
    bsfilter_ids = sql.select([callfilter_table.c.id])

    bsfilter_with_bosses_ids = (sql.select([callfiltermember_table.c.callfilterid])
                                .where(callfiltermember_table.c.bstype == BOSS_TYPE))

    bsfilters_without_bosses = bsfilter_ids.except_(bsfilter_with_bosses_ids)

    return [row.id for row in op.get_bind().execute(bsfilters_without_bosses)]


def delete_bsfilter(bsfilter_id):
    print('[MIGRATE_FK] : Deleting invalid bsfilter with id %s' % bsfilter_id)
    query = (callfiltermember_table
             .delete()
             .where(callfiltermember_table.c.callfilterid == bsfilter_id))

    op.get_bind().execute(query)

    query = (callfilter_table
             .delete()
             .where(callfilter_table.c.id == bsfilter_id))

    op.get_bind().execute(query)

def delete_missing_bsfilter_funckeys():
    template = '[MIGRATE_FK] : Deleting missing bsfilter func key for user "%s" (fk position %s)'
    for row in get_missing_bsfilter_funckeys():
        message = template % (row.iduserfeatures, row.fknum)
        delete_fk(row.iduserfeatures, row.fknum, message)


def delete_fk(iduserfeatures, fknum, message):
    print(message)

    query = (phonefunckey_table
             .delete()
             .where(sql.and_(
                 phonefunckey_table.c.iduserfeatures == iduserfeatures,
                 phonefunckey_table.c.fknum == fknum)))

    op.get_bind().execute(query)


def get_missing_bsfilter_funckeys():
    secretary = callfiltermember_table.alias()
    boss = callfiltermember_table.alias()
    pfk = phonefunckey_table.alias()

    bs_columns = (boss.c.typeval.label('boss_id'),
                  secretary.c.typeval.label('secretary_id'))

    bs_join = boss.join(secretary,
                        sql.and_(
                            secretary.c.bstype == SECRETARY_TYPE,
                            secretary.c.callfilterid == boss.c.callfilterid))

    boss_secretary = (sql.select(bs_columns, from_obj=[bs_join])
                      .where(boss.c.bstype == BOSS_TYPE)
                      .alias())

    pfk_columns = (pfk.c.iduserfeatures,
                   pfk.c.fknum)

    boss_join = pfk.join(boss_secretary,
                         sql.and_(
                             sql.cast(pfk.c.iduserfeatures, sa.Unicode) == boss_secretary.c.boss_id,
                             pfk.c.typevalextenumbersright == boss_secretary.c.secretary_id))

    sec_join = pfk.join(boss_secretary,
                        sql.and_(
                            sql.cast(pfk.c.iduserfeatures, sa.Unicode) == boss_secretary.c.secretary_id,
                            pfk.c.typevalextenumbersright == boss_secretary.c.boss_id))

    all_bsfilters = (sql.select(pfk_columns, from_obj=[boss_join])
                     .union(
                         sql.select(pfk_columns, from_obj=[sec_join]))
                     )

    query = (sql.select(pfk_columns)
             .where(pfk.c.typevalextenumbers == BSFILTER_TYPE)
             .except_(all_bsfilters)
             )

    return op.get_bind().execute(query)


def delete_duplicate_bsfilter_funckeys():
    template = '[MIGRATE_FK] : Deleting duplicate bsfilter func key for user "%s" (fk position %s)'
    for row in get_duplicate_bsfilter_funckeys():
        message = template % (row.iduserfeatures, row.fknum)
        delete_fk(row.iduserfeatures, row.fknum, message)


def get_duplicate_bsfilter_funckeys():
    duplicate_columns = (phonefunckey_table.c.iduserfeatures,
                         phonefunckey_table.c.typevalextenumbersright,
                         sa.func.min(phonefunckey_table.c.fknum).label("first_position"))

    duplicate_query = (sql.select(duplicate_columns)
                       .where(
                           phonefunckey_table.c.typevalextenumbers == BSFILTER_TYPE)
                       .group_by(
                           phonefunckey_table.c.typevalextenumbersright,
                           phonefunckey_table.c.iduserfeatures)
                       .having(
                           sa.func.count(phonefunckey_table.c.typevalextenumbersright) > 1)
                       .alias()
                       )

    columns = (phonefunckey_table.c.iduserfeatures,
               phonefunckey_table.c.fknum)

    join = phonefunckey_table.join(
        duplicate_query,
        sql.and_(
            phonefunckey_table.c.typevalextenumbersright == duplicate_query.c.typevalextenumbersright,
            phonefunckey_table.c.fknum > duplicate_query.c.first_position,
            phonefunckey_table.c.iduserfeatures == duplicate_query.c.iduserfeatures))

    query = sql.select(columns, from_obj=[join])

    return op.get_bind().execute(query)


def create_bsfilter_func_keys():
    for row in get_filter_member_ids():
        create_bsfilter_func_key(row.id)


def get_filter_member_ids():
    bsfilter_query = (sql.select([callfiltermember_table.c.id])
                      .where(
                          callfiltermember_table.c.bstype == SECRETARY_TYPE)
                      )

    return op.get_bind().execute(bsfilter_query)


def create_bsfilter_func_key(filtermember_id):
    func_key_query = (func_key_table
                      .insert()
                      .returning(func_key_table.c.id)
                      .values(type_id=TYPE_ID,
                              destination_type_id=DESTINATION_TYPE_ID)
                      )

    func_key_id = op.get_bind().execute(func_key_query).scalar()

    bsfilter_query = (dest_bsfilter_table
                      .insert()
                      .returning(dest_bsfilter_table.c.func_key_id)
                      .values(func_key_id=func_key_id,
                              destination_type_id=DESTINATION_TYPE_ID,
                              filtermember_id=filtermember_id)
                      )

    op.get_bind().execute(bsfilter_query)

    return func_key_id


def migrate_func_keys():
    for row in get_boss_func_keys():
        func_key_id = find_secretary_func_key(row.boss_id, row.secretary_id)
        create_mapping(func_key_id, row)

    for row in get_secretary_func_keys():
        func_key_id = find_secretary_func_key(row.boss_id, row.secretary_id)
        create_mapping(func_key_id, row)


def get_boss_func_keys():
    columns = (phonefunckey_table.c.iduserfeatures.label('boss_id'),
               phonefunckey_table.c.iduserfeatures.label('user_id'),
               sql.cast(phonefunckey_table.c.typevalextenumbersright, sa.Integer).label('secretary_id'),
               phonefunckey_table.c.fknum.label('position'),
               phonefunckey_table.c.label,
               sql.cast(phonefunckey_table.c.supervision, sa.Boolean).label('blf'))

    join = phonefunckey_table.join(
        callfiltermember_table,
        sql.and_(
            callfiltermember_table.c.bstype == BOSS_TYPE,
            sql.cast(callfiltermember_table.c.typeval, sa.Integer) == phonefunckey_table.c.iduserfeatures)
    )

    query = sql.select(columns, from_obj=[join])

    return op.get_bind().execute(query)


def get_secretary_func_keys():
    columns = (phonefunckey_table.c.iduserfeatures.label('secretary_id'),
               phonefunckey_table.c.iduserfeatures.label('user_id'),
               sql.cast(phonefunckey_table.c.typevalextenumbersright, sa.Integer).label('boss_id'),
               phonefunckey_table.c.fknum.label('position'),
               phonefunckey_table.c.label,
               sql.cast(phonefunckey_table.c.supervision, sa.Boolean).label('blf'))

    join = phonefunckey_table.join(
        callfiltermember_table,
        sql.and_(
            callfiltermember_table.c.bstype == SECRETARY_TYPE,
            sql.cast(callfiltermember_table.c.typeval, sa.Integer) == phonefunckey_table.c.iduserfeatures)
    )

    query = sql.select(columns, from_obj=[join])

    return op.get_bind().execute(query)


def find_secretary_func_key(boss_id, secretary_id):
    filter_query = (sql.select([callfiltermember_table.c.callfilterid])
                    .where(
                        sql.and_(
                            callfiltermember_table.c.bstype == BOSS_TYPE,
                            sql.cast(callfiltermember_table.c.typeval, sa.Integer) == boss_id))
                    )

    filter_id = op.get_bind().execute(filter_query).scalar()

    filter_member_query = (sql.select([callfiltermember_table.c.id])
                           .where(
                               sql.and_(
                                   callfiltermember_table.c.bstype == SECRETARY_TYPE,
                                   sql.cast(callfiltermember_table.c.typeval, sa.Integer) == secretary_id,
                                   callfiltermember_table.c.callfilterid == filter_id))
                           )

    filter_member_id = op.get_bind().execute(filter_member_query).scalar()

    func_key_query = (sql.select([dest_bsfilter_table.c.func_key_id])
                      .where(
                          dest_bsfilter_table.c.filtermember_id == filter_member_id)
                      )

    return op.get_bind().execute(func_key_query).scalar()


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
                             destination_type_id=DESTINATION_TYPE_ID,
                             label=func_key_row.label,
                             position=func_key_row.position,
                             blf=func_key_row.blf))

    conn.execute(mapping_query)


def delete_old_func_keys():
    delete_query = (phonefunckey_table
                    .delete()
                    .where(
                        phonefunckey_table.c.typevalextenumbers == BSFILTER_TYPE)
                    )

    op.get_bind().execute(delete_query)


def downgrade():
    for row in get_old_boss_func_keys():
        create_old_func_key(row)
        delete_mapping(row.func_key_id, row.template_id)

    for row in get_old_secretary_func_keys():
        create_old_func_key(row)
        delete_mapping(row.func_key_id, row.template_id)


def get_old_boss_func_keys():
    columns = (
        func_key_mapping_table.c.func_key_id,
        func_key_mapping_table.c.template_id,
        func_key_mapping_table.c.position,
        func_key_mapping_table.c.blf,
        func_key_mapping_table.c.label,
        callfiltermember_table.c.typeval.label('destination_id'),
        user_table.c.id.label('user_id')
    )

    join = (func_key_mapping_table
            .join(dest_bsfilter_table,
                  func_key_mapping_table.c.func_key_id == dest_bsfilter_table.c.func_key_id)
            .join(template_table,
                  func_key_mapping_table.c.template_id == template_table.c.id)
            .join(user_table,
                  template_table.c.id == user_table.c.func_key_private_template_id)
            .join(callfiltermember_table,
                  callfiltermember_table.c.id == dest_bsfilter_table.c.filtermember_id))

    query = (sql.select(columns, from_obj=[join]))

    return op.get_bind().execute(query)


def get_old_secretary_func_keys():
    boss_filtermember = callfiltermember_table.alias()

    columns = (
        func_key_mapping_table.c.func_key_id,
        func_key_mapping_table.c.template_id,
        func_key_mapping_table.c.position,
        func_key_mapping_table.c.blf,
        func_key_mapping_table.c.label,
        boss_filtermember.c.typeval.label('destination_id'),
        user_table.c.id.label('user_id')
    )

    join_conditions = (func_key_mapping_table
                       .join(dest_bsfilter_table,
                             func_key_mapping_table.c.func_key_id == dest_bsfilter_table.c.func_key_id)
                       .join(template_table,
                             func_key_mapping_table.c.template_id == template_table.c.id)
                       .join(user_table,
                             template_table.c.id == user_table.c.func_key_private_template_id)
                       .join(callfiltermember_table,
                             callfiltermember_table.c.id == dest_bsfilter_table.c.filtermember_id)
                       .join(boss_filtermember,
                             sql.and_(
                                 boss_filtermember.c.bstype == BOSS_TYPE,
                                 boss_filtermember.c.callfilterid == callfiltermember_table.c.callfilterid))
                       )

    query = sql.select(columns, from_obj=[join_conditions])

    return op.get_bind().execute(query)


def create_old_func_key(row):
    supervision = 1 if row.blf else 0

    row = {'iduserfeatures': row.user_id,
           'fknum': row.position,
           'typeextenumbers': 'extenfeatures',
           'typevalextenumbers': 'bsfilter',
           'typeextenumbersright': 'user',
           'typevalextenumbersright': row.destination_id,
           'label': row.label,
           'exten': None,
           'supervision': supervision,
           'progfunckey': 0}

    op.bulk_insert(phonefunckey_table, [row])


def delete_mapping(func_key_id, template_id):
    query = (func_key_mapping_table
             .delete()
             .where(sql.and_(
                 func_key_mapping_table.c.func_key_id == func_key_id,
                 func_key_mapping_table.c.template_id == template_id)))

    op.get_bind().execute(query)
