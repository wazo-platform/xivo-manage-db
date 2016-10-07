"""add a wizard webservice access

Revision ID: 21d45c24210e
Revises: 341f7e584088

"""

# revision identifiers, used by Alembic.
revision = '21d45c24210e'
down_revision = '341f7e584088'

from alembic import op
from sqlalchemy import sql, func

webservice = sql.table('accesswebservice',
                       sql.column('name'),
                       sql.column('login'),
                       sql.column('passwd'),
                       sql.column('acl'))
ACL = '{dird.tenants.*.phonebooks.create}'


def upgrade():
    op.execute(webservice
               .insert()
               .values(name='xivo-wizard',
                       login='xivo-wizard',
                       passwd=func.substring(func.gen_salt('bf', 4), 8),
                       acl=ACL))


def downgrade():
    op.execute(webservice.delete().where(webservice.c.name == 'xivo-wizard'))

