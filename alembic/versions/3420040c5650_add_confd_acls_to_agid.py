"""add_confd_acls_to_agid

Revision ID: 3420040c5650
Revises: 7f1c1c00662

"""

from alembic import op
from sqlalchemy import sql
from sqlalchemy.dialects.postgresql import ARRAY, VARCHAR

# revision identifiers, used by Alembic.
revision = '3420040c5650'
down_revision = '7f1c1c00662'


accesswebservice = sql.table('accesswebservice',
                             sql.column('id'),
                             sql.column('name'),
                             sql.column('acl'))

ACLS = ['confd.lines.read',
        'confd.devices.read',
        'confd.lines.*.devices.*.update',
        'confd.devices.*.synchronize.read']


def upgrade():
    acls = sql.cast(ACLS, ARRAY(VARCHAR))
    query = (accesswebservice
             .update()
             .values(
                 acl=sql.func.array_cat(accesswebservice.c.acl, acls))
             .where(
                 accesswebservice.c.name == "xivo-agid"))
    op.execute(query)


def downgrade():
    for acl in ACLS:
        query = (accesswebservice
                 .update()
                 .values(
                     acl=sql.func.array_remove(accesswebservice.c.acl, acl))
                 .where(
                     accesswebservice.c.name == "xivo-agid"))
        op.execute(query)
