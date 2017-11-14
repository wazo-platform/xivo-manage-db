"""update wazo-plugind-cli ACL

Revision ID: 5b427e206bdf
Revises: 6aead6a54bbb

"""

# revision identifiers, used by Alembic.
revision = '5b427e206bdf'
down_revision = '6aead6a54bbb'

from alembic import op
from sqlalchemy import sql
from sqlalchemy.dialects.postgres import ARRAY, VARCHAR

webservice = sql.table('accesswebservice',
                       sql.column('id'),
                       sql.column('name'),
                       sql.column('acl'))

SERVICE = 'wazo-plugind-cli'
OLD_ACLS = ['plugind.plugins.create', 'plugind.plugins.*.*.delete', 'plugind.plugins.read']
NEW_ACLS = ['plugind.#']


def upgrade():
    _remove_acls(SERVICE, OLD_ACLS)
    _add_acls(SERVICE, NEW_ACLS)


def downgrade():
    _remove_acls(SERVICE, NEW_ACLS)
    _add_acls(SERVICE, OLD_ACLS)


def _add_acls(name, acls):
    acl = sql.cast(acls, ARRAY(VARCHAR))
    query = (webservice
        .update()
        .values(
        acl=sql.func.array_cat(webservice.c.acl, acl))
        .where(
        webservice.c.name == name))
    op.execute(query)


def _remove_acls(name, acls):
    for acl in acls:
        query = (webservice
            .update()
            .values(
            acl=sql.func.array_remove(webservice.c.acl, acl))
            .where(
            webservice.c.name == name))
        op.execute(query)
