"""add_wazo_upgrade_acl

Revision ID: 2251b5ae9e6c
Revises: 41a523e18fdd

"""

from alembic import op
from sqlalchemy import sql, func

# revision identifiers, used by Alembic.
revision = '2251b5ae9e6c'
down_revision = '41a523e18fdd'

webservice = sql.table('accesswebservice',
                       sql.column('name'),
                       sql.column('login'),
                       sql.column('passwd'),
                       sql.column('acl'),
                       sql.column('description'))
ACL = '{plugind.#,confd.#,auth.#}'
DESCRIPTION = 'Automatically created during upgrade'
SERVICE = 'wazo-upgrade'


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
