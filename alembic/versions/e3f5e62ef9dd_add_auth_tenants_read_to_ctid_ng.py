"""add auth.tenants.read to ctid-ng

Revision ID: e3f5e62ef9dd
Revises: 0d74d34f7782

"""

from alembic import op
from sqlalchemy import sql
from sqlalchemy.dialects.postgresql import ARRAY, VARCHAR

# revision identifiers, used by Alembic.
revision = 'e3f5e62ef9dd'
down_revision = '0d74d34f7782'


accesswebservice = sql.table('accesswebservice',
                             sql.column('id'),
                             sql.column('name'),
                             sql.column('acl'))

ACLS = ['auth.tenants.read']
SERVICE = 'xivo-ctid-ng'


def upgrade():
    acls = sql.cast(ACLS, ARRAY(VARCHAR))
    query = (accesswebservice
             .update()
             .values(
                 acl=sql.func.array_cat(accesswebservice.c.acl, acls))
             .where(
                 accesswebservice.c.name == SERVICE))
    op.execute(query)


def downgrade():
    for acl in ACLS:
        query = (accesswebservice
                 .update()
                 .values(
                     acl=sql.func.array_remove(accesswebservice.c.acl, acl))
                 .where(
                     accesswebservice.c.name == SERVICE))
        op.execute(query)
