"""add xivo-auth web service

Revision ID: 415b08ed9959
Revises: 1ddfb39a066f

"""

# revision identifiers, used by Alembic.
revision = '415b08ed9959'
down_revision = '1ddfb39a066f'

from alembic import op
from sqlalchemy import sql, func


webservice = sql.table('accesswebservice',
                       sql.column('name'),
                       sql.column('login'),
                       sql.column('passwd'),
                       sql.column('acl'))
ACL = '{confd.users.read}'
SERVICE = 'xivo-auth'


def upgrade():
    op.execute(webservice
               .insert()
               .values(name=SERVICE,
                       login=SERVICE,
                       passwd=func.substring(func.gen_salt('bf', 4), 8),
                       acl=ACL))


def downgrade():
    op.execute(webservice.delete().where(webservice.c.name == SERVICE))
