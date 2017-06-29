"""add wazo-plugind acl

Revision ID: bc9e62985a0
Revises: 17653c3f37ce

"""

# revision identifiers, used by Alembic.
revision = 'bc9e62985a0'
down_revision = '17653c3f37ce'

from alembic import op
from sqlalchemy import sql, func


webservice = sql.table('accesswebservice',
                       sql.column('name'),
                       sql.column('login'),
                       sql.column('passwd'),
                       sql.column('acl'),
                       sql.column('description'))
ACL = '{confd.infos.read}'
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
