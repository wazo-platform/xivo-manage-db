"""add xivo-auth web service

Revision ID: 3e6bc9ae6158
Revises: d9e7aac4970

"""

# revision identifiers, used by Alembic.
revision = '3e6bc9ae6158'
down_revision = 'd9e7aac4970'

from alembic import op
from sqlalchemy import sql, func


webservice = sql.table('accesswebservice',
                       sql.column('name'),
                       sql.column('login'),
                       sql.column('passwd'),
                       sql.column('acl'),
                       sql.column('description'))
ACL = '{confd.lines.read}'
DESCRIPTION = 'Automatically created during upgrade'
SERVICE = 'xivo-call-logd'


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
