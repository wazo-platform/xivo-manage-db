"""add ACLs to xivo-ctid-ng


Revision ID: 3133fb4958ef
Revises: 1b6be5d5e4ac

"""

# revision identifiers, used by Alembic.
revision = '3133fb4958ef'
down_revision = '1b6be5d5e4ac'

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
                            '{confd.#, amid.action.Redirect.create, amid.action.Setvar.create}')


def _update_web_service_acl(name, acl):
    op.execute(webservice
               .update()
               .where(
                   webservice.c.name == name
               ).values(acl=acl))


def downgrade():
    _update_web_service_acl('xivo-ctid-ng',
                            '{confd.#}')
