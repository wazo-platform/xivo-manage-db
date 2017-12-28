"""add_users_confd_acl_to_call_logd

Revision ID: b5f230e1e0fe
Revises: 15fb16c0b0f8

"""

# revision identifiers, used by Alembic.
revision = 'b5f230e1e0fe'
down_revision = '15fb16c0b0f8'

from alembic import op
from sqlalchemy import sql


webservice = sql.table('accesswebservice',
                       sql.column('name'),
                       sql.column('acl'))

SERVICE = 'xivo-call-logd'
NEW_ACL = set(['confd.users.*.read'])


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
