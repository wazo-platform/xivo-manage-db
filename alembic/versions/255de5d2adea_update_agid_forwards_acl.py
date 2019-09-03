"""update_agid_forwards_acl

Revision ID: 255de5d2adea
Revises: 13f4485996fd

"""

from alembic import op
from sqlalchemy import sql
from sqlalchemy.dialects.postgresql import ARRAY, VARCHAR

# revision identifiers, used by Alembic.
revision = '255de5d2adea'
down_revision = '13f4485996fd'

accesswebservice = sql.table('accesswebservice',
                             sql.column('id'),
                             sql.column('name'),
                             sql.column('acl'))

OLD_ACLS = ['confd.users.*.forwards.*.*']
NEW_ACLS = ['confd.users.*.forwards.#']


def upgrade():
    _remove_acls('xivo-agid', OLD_ACLS)
    _add_acls('xivo-agid', NEW_ACLS)


def downgrade():
    _remove_acls('xivo-agid', NEW_ACLS)
    _add_acls('xivo-agid', OLD_ACLS)


def _add_acls(name, acls):
    acl = sql.cast(acls, ARRAY(VARCHAR))
    query = (accesswebservice
             .update()
             .values(
                 acl=sql.func.array_cat(accesswebservice.c.acl, acl))
             .where(
                 accesswebservice.c.name == name))
    op.execute(query)


def _remove_acls(name, acls):
    for acl in acls:
        query = (accesswebservice
                 .update()
                 .values(
                     acl=sql.func.array_remove(accesswebservice.c.acl, acl))
                 .where(
                     accesswebservice.c.name == name))
        op.execute(query)
