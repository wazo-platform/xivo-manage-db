"""add wazo-plugind-cli acl

Revision ID: 324ad441b84c
Revises: 13472f54a7

"""

# revision identifiers, used by Alembic.
revision = '324ad441b84c'
down_revision = '13472f54a7'

from alembic import op
from sqlalchemy import sql, func


webservice = sql.table('accesswebservice',
                       sql.column('name'),
                       sql.column('login'),
                       sql.column('passwd'),
                       sql.column('acl'),
                       sql.column('description'))
ACL = '{plugind.plugins.create, plugind.plugins.*.*.delete}'
DESCRIPTION = 'Automatically created during upgrade'
SERVICE = 'wazo-plugind'


def upgrade():
    op.execute(webservice
               .insert()
               .values(name=SERVICE,
                       login=SERVICE,
                       passwd=func.substring(func.gen_salt('bf', 4), 8),
                       acl=ACL,
                       description=DESCRIPTION))


def downgrade():
    op.execute(webservice.delete().where(webservice.c.name == SERVICE))
