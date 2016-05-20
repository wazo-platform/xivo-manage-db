"""add ACLs to xivo-ctid-ng

Revision ID: b8d0848e7b2
Revises: 2c940e077157

"""

# revision identifiers, used by Alembic.
revision = 'b8d0848e7b2'
down_revision = '2c940e077157'

from alembic import op
from sqlalchemy import sql


webservice = sql.table('accesswebservice',
                       sql.column('name'),
                       sql.column('login'),
                       sql.column('passwd'),
                       sql.column('acl'),
                       sql.column('description'))


def upgrade():
    _update_web_service_acl('xivo-ctid-ng',
                            '{confd.#, amid.action.Redirect.create, amid.action.ShowDialplan.create, amid.action.Setvar.create}')


def _update_web_service_acl(name, acl):
    op.execute(webservice
               .update()
               .where(
                   webservice.c.name == name
               ).values(acl=acl))


def downgrade():
    _update_web_service_acl('xivo-ctid-ng',
                            '{confd.#, amid.action.Redirect.create, amid.action.Setvar.create}')
