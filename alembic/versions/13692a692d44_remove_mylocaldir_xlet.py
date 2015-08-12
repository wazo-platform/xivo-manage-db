"""remove_mylocaldir_xlet

Revision ID: 13692a692d44
Revises: 44c6b8d8c196

"""

# revision identifiers, used by Alembic.
revision = '13692a692d44'
down_revision = '44c6b8d8c196'

from alembic import op
import sqlalchemy as sa
from sqlalchemy import sql


MYLOCALDIR_XLET = 'mylocaldir'
PEOPLE_XLET = 'people'

xlet_table = sa.sql.table('cti_xlet',
                          sa.sql.column('id'),
                          sa.sql.column('plugin_name'))
profile_xlet_table = sa.sql.table('cti_profile_xlet',
                                  sa.sql.column('profile_id'),
                                  sa.sql.column('xlet_id'))


def upgrade():
    replace_xlet_with_people()
    remove_xlet()


def downgrade():
    create_xlet()


def replace_xlet_with_people():
    people_id = _xlet_id(PEOPLE_XLET)
    mylocaldir_id = _xlet_id(MYLOCALDIR_XLET)
    profiles_with_people_query = (
        sa.sql.select(
            [profile_xlet_table.c.profile_id]
        ).where(profile_xlet_table.c.xlet_id == people_id)
    )

    # replace mylocaldir with people if people is not already in profile
    replace_query = (
        profile_xlet_table
        .update()
        .values(xlet_id=people_id)
        .where(sa.sql.and_(
            profile_xlet_table.c.xlet_id == mylocaldir_id,
            ~profile_xlet_table.c.profile_id.in_(profiles_with_people_query),
        ))
    )
    op.execute(replace_query)


def _xlet_id(xlet_name):
    return op.get_bind().execute(
        sql.select(
            [xlet_table.c.id])
        .where(
            xlet_table.c.plugin_name == xlet_name)
    ).scalar()


def remove_xlet():
    remove_xlet_query = (xlet_table
                         .delete()
                         .where(xlet_table.c.plugin_name == MYLOCALDIR_XLET))
    op.execute(remove_xlet_query)


def create_xlet():
    create_xlet_query = (xlet_table
                         .insert()
                         .values(plugin_name=MYLOCALDIR_XLET))
    op.execute(create_xlet_query)
