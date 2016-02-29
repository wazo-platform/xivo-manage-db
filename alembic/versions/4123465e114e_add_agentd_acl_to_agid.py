"""add_agentd_acl_to_agid

Revision ID: 4123465e114e
Revises: 2903faf08938

"""

# revision identifiers, used by Alembic.
revision = '4123465e114e'
down_revision = '2903faf08938'

from alembic import op
from sqlalchemy import sql

webservice = sql.table('accesswebservice',
                       sql.column('name'),
                       sql.column('acl'))


def upgrade():
    _update_web_service_acl('xivo-agid',
                            '{dird.directories.reverse.*.*.read, agentd.#}')


def downgrade():
    _update_web_service_acl('xivo-agid',
                            '{dird.directories.reverse.*.*.read}')


def _update_web_service_acl(name, acl):
    op.execute(webservice
               .update()
               .where(
                   webservice.c.name == name
               ).values(acl=acl))
