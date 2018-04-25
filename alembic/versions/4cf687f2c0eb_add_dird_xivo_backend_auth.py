"""add dird-xivo-backend auth

Revision ID: 4cf687f2c0eb
Revises: 52acaaba550c

"""

# revision identifiers, used by Alembic.
revision = '4cf687f2c0eb'
down_revision = '52acaaba550c'


from alembic import op
from sqlalchemy import sql, func


webservice = sql.table('accesswebservice',
                       sql.column('name'),
                       sql.column('login'),
                       sql.column('passwd'),
                       sql.column('acl'),
                       sql.column('description'))
ACL = '{confd.users.read, confd.infos.read}'
DESCRIPTION = 'Automatically created during upgrade'
SERVICE = 'wazo-dird-xivo-backend'


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
