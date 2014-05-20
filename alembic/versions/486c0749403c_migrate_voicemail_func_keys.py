"""migrate_voicemail_func_keys

Revision ID: 486c0749403c
Revises: 55f3c86885c5
Create Date: 2014-05-14 15:34:14.127634
XiVO Version: <version>

"""

# revision identifiers, used by Alembic.
revision = '486c0749403c'
down_revision = '55f3c86885c5'

from alembic import op
import sqlalchemy as sa


TYPE_SPEEDDIAL = 'speeddial'

DESTINATION_EXTENSION_ID = 5
DESTINATION_EXTENSION_NAME = 'extension'

phonefunckey_table = sa.sql.table('phonefunckey',
                                  sa.sql.column('iduserfeatures'),
                                  sa.sql.column('fknum'),
                                  sa.sql.column('exten'),
                                  sa.sql.column('typeextenumbers'),
                                  sa.sql.column('typevalextenumbers'),
                                  sa.sql.column('typeextenumbersright'),
                                  sa.sql.column('typevalextenumbersright'),
                                  sa.sql.column('label'),
                                  sa.sql.column('supervision'),
                                  sa.sql.column('progfunckey'))

func_key_table = sa.sql.table('func_key',
                              sa.sql.column('id'),
                              sa.sql.column('type_id'),
                              sa.sql.column('destination_type_id'))

destination_extension_table = sa.sql.table('func_key_dest_extension',
                                           sa.sql.column('func_key_id'),
                                           sa.sql.column('destination_type_id'),
                                           sa.sql.column('extension_id'))

func_key_type_table = sa.sql.table('func_key_type',
                                   sa.sql.column('id'),
                                   sa.sql.column('name'))

func_key_mapping_table = sa.sql.table('func_key_mapping',
                                      sa.sql.column('template_id'),
                                      sa.sql.column('func_key_id'),
                                      sa.sql.column('destination_type_id'),
                                      sa.sql.column('label'),
                                      sa.sql.column('position'),
                                      sa.sql.column('blf'))

template_table = sa.sql.table('func_key_template',
                              sa.sql.column('id'))

extensions_table = sa.sql.table('extensions',
                                sa.sql.column('id'),
                                sa.sql.column('commented'),
                                sa.sql.column('context'),
                                sa.sql.column('exten'),
                                sa.sql.column('type'),
                                sa.sql.column('typeval'))

user_table = sa.sql.table('userfeatures',
                          sa.sql.column('id'),
                          sa.sql.column('func_key_private_template_id'))

destination_type_table = sa.sql.table('func_key_destination_type',
                                      sa.sql.column('id'),
                                      sa.sql.column('name'))

blf_cast = sa.sql.cast(phonefunckey_table.c.supervision, sa.Boolean)

voicemail_func_keys_query = (sa.sql.select([phonefunckey_table.c.iduserfeatures.label('user_id'),
                                            phonefunckey_table.c.fknum.label('position'),
                                            phonefunckey_table.c.label,
                                            phonefunckey_table.c.typevalextenumbers,
                                            blf_cast.label('blf')])
                             .where(phonefunckey_table.c.typevalextenumbers
                                    .in_(('enablevm', 'vmusermsg', 'vmuserpurge'))))


old_func_keys_query = (sa.sql.select([func_key_mapping_table.c.func_key_id,
                                      func_key_mapping_table.c.template_id,
                                      func_key_mapping_table.c.position,
                                      func_key_mapping_table.c.blf,
                                      func_key_mapping_table.c.label,
                                      destination_extension_table.c.extension_id,
                                      extensions_table.c.typeval,
                                      user_table.c.id.label('user_id')],
                                     from_obj=[
                                         func_key_mapping_table.join(
                                             destination_extension_table,
                                             func_key_mapping_table.c.func_key_id == destination_extension_table.c.func_key_id)
                                         .join(extensions_table,
                                               destination_extension_table.c.extension_id == extensions_table.c.id)
                                         .join(template_table,
                                               func_key_mapping_table.c.template_id == template_table.c.id)
                                         .join(user_table,
                                               template_table.c.id == user_table.c.func_key_private_template_id)]
                                     ))


def upgrade():
    for row in op.get_bind().execute(voicemail_func_keys_query):
        func_key_id = _create_func_key()
        extension_id = _get_extension_id_from_type(row.typevalextenumbers)
        _create_extension_destination(func_key_id, extension_id)
        _create_mapping(func_key_id, row)

    _delete_old_func_keys()


def _create_func_key():
    speeddial_id = _get_speeddial_id()
    insert_query = (func_key_table
                    .insert()
                    .returning(func_key_table.c.id)
                    .values(type_id=speeddial_id,
                            destination_type_id=DESTINATION_EXTENSION_ID))

    return op.get_bind().execute(insert_query).first()[0]


def _get_speeddial_id():
    return op.get_bind().execute(
        sa.sql.select(
            [func_key_type_table.c.id])
        .where(
            func_key_type_table.c.name == TYPE_SPEEDDIAL)
    ).scalar()


def _get_extension_id_from_type(vmtype):
    return op.get_bind().execute(
        sa.sql.select(
            [extensions_table.c.id])
        .where(
            extensions_table.c.typeval == vmtype)
    ).scalar()


def _create_extension_destination(func_key_id, extension_id):
    destination_query = (destination_extension_table
                         .insert()
                         .returning(destination_extension_table.c.func_key_id)
                         .values(func_key_id=func_key_id,
                                 destination_type_id=DESTINATION_EXTENSION_ID,
                                 extension_id=extension_id))

    op.get_bind().execute(destination_query)


def _create_mapping(func_key_id, func_key_row):
    conn = op.get_bind()

    template_id = conn.execute(sa.sql.select(
        [user_table.c.func_key_private_template_id])
        .where(
            user_table.c.id == func_key_row.user_id)
    ).scalar()

    mapping_query = (func_key_mapping_table
                     .insert()
                     .returning(func_key_mapping_table.c.func_key_id)
                     .values(func_key_id=func_key_id,
                             template_id=template_id,
                             destination_type_id=DESTINATION_EXTENSION_ID,
                             label=func_key_row.label,
                             position=func_key_row.position,
                             blf=func_key_row.blf))

    conn.execute(mapping_query)


def _delete_old_func_keys():
    delete_query = (phonefunckey_table
                    .delete()
                    .where(phonefunckey_table.c.typevalextenumbers
                           .in_(('enablevm', 'vmusermsg', 'vmuserpurge', 'enablevmbox'))))

    op.get_bind().execute(delete_query)


def downgrade():
    for row in op.get_bind().execute(old_func_keys_query):
        _create_old_func_keys(row)
        _delete_destination(row.func_key_id, row.extension_id)
        _delete_mapping(row.func_key_id, row.template_id)
        _delete_func_key(row.func_key_id)


def _create_old_func_keys(row):
    supervision = 1 if row.blf else 0

    row = {'iduserfeatures': row.user_id,
           'fknum': row.position,
           'typevalextenumbers': row.typeval,
           'typeextenumbersright': None,
           'typevalextenumbersright': None,
           'label': row.label,
           'supervision': supervision}

    op.bulk_insert(phonefunckey_table, [row])


def _delete_destination(func_key_id, extension_id):
    query = (destination_extension_table
             .delete()
             .where(sa.sql.and_(
                 destination_extension_table.c.func_key_id == func_key_id,
                 destination_extension_table.c.extension_id == extension_id)))

    op.get_bind().execute(query)


def _delete_mapping(func_key_id, template_id):
    query = (func_key_mapping_table
             .delete()
             .where(sa.sql.and_(
                 func_key_mapping_table.c.func_key_id == func_key_id,
                 func_key_mapping_table.c.template_id == template_id)))

    op.get_bind().execute(query)


def _delete_func_key(func_key_id):
    query = (func_key_table
             .delete()
             .where(func_key_table.c.id == func_key_id))

    op.get_bind().execute(query)
