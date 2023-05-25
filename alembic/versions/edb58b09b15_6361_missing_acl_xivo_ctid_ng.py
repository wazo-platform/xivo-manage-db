"""6361-missing-acl-xivo-ctid-ng

Revision ID: edb58b09b15
Revises: 333cd1b1d31

This revision duplicates revision b8d0848e7b2 to fix a desynchronisation between
a fresh install and an upgraded database. See bug #6361.

"""

# revision identifiers, used by Alembic.
revision = 'edb58b09b15'
down_revision = '333cd1b1d31'

from alembic import op
from sqlalchemy import sql


webservice = sql.table('accesswebservice',
                       sql.column('name'),
                       sql.column('acl'))

SERVICE = 'xivo-ctid-ng'
NEW_ACL = {'amid.action.ShowDialplan.create'}


def upgrade():
    current_acls = _get_current_acl(SERVICE)
    new_acls = current_acls | NEW_ACL
    _update_web_service_acl(SERVICE, new_acls)


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


def downgrade():
    current_acls = _get_current_acl(SERVICE)
    new_acls = current_acls - NEW_ACL
    _update_web_service_acl(SERVICE, new_acls)
