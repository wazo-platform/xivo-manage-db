"""add xivo-ctid-ng acl

Revision ID: 4977a626c01
Revises: 2989b8b30fe7

"""

# revision identifiers, used by Alembic.
revision = '4977a626c01'
down_revision = '2989b8b30fe7'

from alembic import op
from sqlalchemy import sql


webservice = sql.table('accesswebservice',
                       sql.column('name'),
                       sql.column('acl'))

SERVICE = 'xivo-ctid-ng'
NEW_ACL = set(['amid.action.Command.create'])


def _get_current_acl(name):
    return set(op.get_bind().execute(
        sql.select([webservice.c.acl]).where(webservice.c.name == name)
    ).scalar())


def _update_web_service_acl(name, acl):
    op.execute(webservice
               .update()
               .where(
                   webservice.c.name == name
               ).values(acl=list(acl)))


def upgrade():
    current_acls = _get_current_acl(SERVICE)
    new_acls = current_acls | NEW_ACL
    _update_web_service_acl(SERVICE, new_acls)


def downgrade():
    current_acls = _get_current_acl(SERVICE)
    new_acls = current_acls - NEW_ACL
    _update_web_service_acl(SERVICE, new_acls)
