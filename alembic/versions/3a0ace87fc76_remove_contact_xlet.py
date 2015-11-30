"""remove contact xlet

Revision ID: 3a0ace87fc76
Revises: 2f7e5c4119bc

"""

# revision identifiers, used by Alembic.
revision = '3a0ace87fc76'
down_revision = '2f7e5c4119bc'

from alembic import op
import sqlalchemy as sa


CONTACT_XLET = 'search'
PEOPLE_XLET = 'people'


xlet_table = sa.sql.table('cti_xlet',
                          sa.sql.column('id'),
                          sa.sql.column('plugin_name'))
profile_xlet_table = sa.sql.table('cti_profile_xlet',
                                  sa.sql.column('profile_id'),
                                  sa.sql.column('xlet_id'))


def get_xlet_id(xlet_name):
    return op.get_bind().execute(
        sa.sql.select(
            [xlet_table.c.id]
        ).where(
            xlet_table.c.plugin_name == xlet_name
        )).scalar()


def find_profile_with_xlet(xlet_id):
    rows = op.get_bind().execute(
        sa.sql.select(
            [profile_xlet_table.c.profile_id]
        ).where(
            profile_xlet_table.c.xlet_id == xlet_id
        ))

    return list(set(row.profile_id for row in rows))


def substitute_xlet(profile_ids, from_id, to_id):
    if not profile_ids:
        return
    op.execute(profile_xlet_table.update()
               .values(xlet_id=to_id)
               .where(sa.and_(profile_xlet_table.c.xlet_id == from_id,
                              profile_xlet_table.c.profile_id.in_(profile_ids))))


def remove_xlet(xlet_id):
    op.execute(xlet_table.delete().where(xlet_table.c.id == xlet_id))


def create_xlet_contact():
    op.execute(xlet_table.insert().values(plugin_name=CONTACT_XLET))


def upgrade():
    contact_id = get_xlet_id(CONTACT_XLET)
    people_id = get_xlet_id(PEOPLE_XLET)

    profile_ids_with_contact = find_profile_with_xlet(contact_id)
    profile_ids_with_people = find_profile_with_xlet(people_id)
    profile_ids_with_contact_only = list(set(profile_ids_with_contact) - set(profile_ids_with_people))

    substitute_xlet(profile_ids_with_contact_only, contact_id, people_id)
    remove_xlet(contact_id)


def downgrade():
    create_xlet_contact()
