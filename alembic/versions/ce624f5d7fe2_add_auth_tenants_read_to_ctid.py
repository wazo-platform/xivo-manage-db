"""add_auth_tenants_read_to_ctid

Revision ID: ce624f5d7fe2
Revises: 778dc763148f

"""

from alembic import op
from sqlalchemy import sql
from sqlalchemy.dialects.postgresql import ARRAY, VARCHAR

# revision identifiers, used by Alembic.
revision = 'ce624f5d7fe2'
down_revision = '778dc763148f'

accesswebservice = sql.table(
    'accesswebservice',
    sql.column('id'),
    sql.column('name'),
    sql.column('acl'),
)

ACLS = ['auth.tenants.read']
SERVICE = 'xivo-ctid'


def upgrade():
    acls = sql.cast(ACLS, ARRAY(VARCHAR))
    query = (
        accesswebservice
        .update()
        .values(
            acl=sql.func.array_cat(accesswebservice.c.acl, acls))
        .where(
            accesswebservice.c.name == SERVICE)
    )
    op.execute(query)


def downgrade():
    for acl in ACLS:
        query = (
            accesswebservice
            .update()
            .values(
                acl=sql.func.array_remove(accesswebservice.c.acl, acl))
            .where(
                accesswebservice.c.name == SERVICE)
        )
        op.execute(query)
