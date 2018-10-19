"""add the asterisk service user

Revision ID: 6545d103068c
Revises: 74a76197acaa

"""

from alembic import op
from sqlalchemy import sql, func


# revision identifiers, used by Alembic.
revision = '6545d103068c'
down_revision = '74a76197acaa'

webservice = sql.table('accesswebservice',
                       sql.column('name'),
                       sql.column('login'),
                       sql.column('passwd'),
                       sql.column('acl'),
                       sql.column('description'))
ACL = '{auth.tenants.read, confd.voicemails.read, confd.voicemails.*.update}'
DESCRIPTION = 'Automatically created during upgrade'
SERVICE = 'asterisk'


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
