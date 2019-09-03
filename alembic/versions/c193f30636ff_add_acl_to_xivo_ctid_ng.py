"""add acl to xivo-ctid-ng

Revision ID: c193f30636ff
Revises: 40e2f31cf146

"""

from alembic import op
from sqlalchemy import sql
from sqlalchemy.dialects.postgresql import ARRAY, VARCHAR


# revision identifiers, used by Alembic.
revision = 'c193f30636ff'
down_revision = '40e2f31cf146'

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
