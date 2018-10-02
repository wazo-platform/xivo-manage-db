"""add_auth_tenants_read_to_dird

Revision ID: 778dc763148f
Revises: 6afcf16a334d

"""

from alembic import op
from sqlalchemy import sql
from sqlalchemy.dialects.postgres import ARRAY, VARCHAR

# revision identifiers, used by Alembic.
revision = '778dc763148f'
down_revision = '6afcf16a334d'

accesswebservice = sql.table(
    'accesswebservice',
    sql.column('id'),
    sql.column('name'),
    sql.column('acl'),
)

ACLS = ['auth.tenants.read']
SERVICE = 'wazo-dird-xivo-backend'


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
