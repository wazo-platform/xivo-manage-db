"""add_mongooseim_acl_to_ctid_ng

Revision ID: 2984e5ede175
Revises: 52b66f888125

"""

from alembic import op
from sqlalchemy import sql
from sqlalchemy.dialects.postgres import ARRAY, VARCHAR

# revision identifiers, used by Alembic.
revision = '2984e5ede175'
down_revision = '52b66f888125'

accesswebservice = sql.table('accesswebservice',
                             sql.column('id'),
                             sql.column('name'),
                             sql.column('acl'))

NEW_ACLS = ['websocketd', 'websocketd.#', 'mongooseim.admin']


def upgrade():
    _add_acls('xivo-ctid-ng', NEW_ACLS)


def downgrade():
    _remove_acls('xivo-ctid-ng', NEW_ACLS)


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
