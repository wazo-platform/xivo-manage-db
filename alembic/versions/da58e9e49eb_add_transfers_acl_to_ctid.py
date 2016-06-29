"""add transfers acl to ctid

Revision ID: da58e9e49eb
Revises: 564d634619bc

"""

# revision identifiers, used by Alembic.
revision = 'da58e9e49eb'
down_revision = '564d634619bc'


from alembic import op
from sqlalchemy import sql


webservice = sql.table('accesswebservice',
                       sql.column('name'),
                       sql.column('acl'))

SERVICE = 'xivo-ctid'
NEW_ACL = set(['ctid-ng.transfers.#'])


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
