"""add tenants acl to the wizard

Revision ID: 3462497a56f8
Revises: 01b4c79b3d47

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '3462497a56f8'
down_revision = '01b4c79b3d47'

webservice = sql.table('accesswebservice',
                       sql.column('name'),
                       sql.column('acl'))

SERVICE = 'xivo-wizard'
NEW_ACL = set(['auth.tenants.create'])


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
