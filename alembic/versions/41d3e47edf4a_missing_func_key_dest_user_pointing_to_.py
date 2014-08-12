"""Missing func_key_dest_user_pointing_to_users

Revision ID: 41d3e47edf4a
Revises: 58e808b69aec
XiVO Version: <version>

"""

# revision identifiers, used by Alembic.
revision = '41d3e47edf4a'
down_revision = '58e808b69aec'

from alembic import op
import sqlalchemy as sa


TYPE_SPEEDDIAL = 'speeddial'

DESTINATION_USER_ID = 1
DESTINATION_USER_NAME = 'user'


userfeatures_table = sa.sql.table('userfeatures',
                                  sa.sql.column('id'),
                                  sa.sql.column('func_key_private_template_id'))

func_key_table = sa.sql.table('func_key',
                              sa.sql.column('id'),
                              sa.sql.column('type_id'),
                              sa.sql.column('destination_type_id'))

func_key_type_table = sa.sql.table('func_key_type',
                                   sa.sql.column('id'),
                                   sa.sql.column('name'))

destination_type_table = sa.sql.table('func_key_destination_type',
                                      sa.sql.column('id'),
                                      sa.sql.column('name'))

destination_user_table = sa.sql.table('func_key_dest_user',
                                      sa.sql.column('func_key_id'),
                                      sa.sql.column('destination_type_id'),
                                      sa.sql.column('user_id'))

userfeatures_table_query = (sa.sql.select(
    [userfeatures_table.c.id,
     userfeatures_table.c.func_key_private_template_id]))

destination_user_table_query = (sa.sql.select([destination_user_table.c.func_key_id,
                                               destination_user_table.c.destination_type_id,
                                               destination_user_table.c.user_id]))

func_key_table_query = (sa.sql.select([func_key_table.c.id,
                                       func_key_table.c.type_id,
                                       func_key_table.c.destination_type_id])
                        .where(func_key_table.c.destination_type_id == DESTINATION_USER_ID))


def upgrade():
    for user in _get_users():
        if _get_fk_id_dst_user_with_user_id(user.id) is None:
            _create_func_key_for_user(user.id)

    _clean_orphan_func_key()


def _get_speeddial_id():
    return op.get_bind().execute(
        sa.sql.select(
            [func_key_type_table.c.id])
        .where(
            func_key_type_table.c.name == TYPE_SPEEDDIAL)
    ).scalar()


def _get_users():
    return op.get_bind().execute(userfeatures_table_query)


def _get_all_user_func_key():
    return op.get_bind().execute(func_key_table_query)


def _get_fk_id_dst_user_with_user_id(user_id):
    return op.get_bind().execute(
        sa.sql.select(
            [destination_user_table.c.func_key_id])
        .where(
            destination_user_table.c.user_id == user_id)
    ).scalar()


def _get_user_id_with_func_key_id(fk_id):
    return op.get_bind().execute(
        sa.sql.select(
            [destination_user_table.c.user_id])
        .where(
            destination_user_table.c.func_key_id == fk_id)
    ).scalar()


def _create_func_key():
    speeddial_id = _get_speeddial_id()
    insert_query = (func_key_table
                    .insert()
                    .returning(func_key_table.c.id)
                    .values(type_id=speeddial_id,
                            destination_type_id=DESTINATION_USER_ID))

    return op.get_bind().execute(insert_query).scalar()


def _create_func_key_for_user(user_id):
    func_key_id = _create_func_key()
    insert_query = (destination_user_table
                    .insert()
                    .returning(destination_user_table.c.user_id)
                    .values(func_key_id=func_key_id,
                            user_id=user_id,
                            destination_type_id=DESTINATION_USER_ID))

    return op.get_bind().execute(insert_query).scalar()


def _clean_orphan_func_key():
    for fk in _get_all_user_func_key():
        if _get_user_id_with_func_key_id(fk.id) is None:
            _delete_func_key_with_id(fk.id)


def _delete_func_key_with_id(fk_id):
    query = (func_key_table
             .delete()
             .where(func_key_table.c.id == fk_id))

    op.get_bind().execute(query)


def downgrade():
    pass
