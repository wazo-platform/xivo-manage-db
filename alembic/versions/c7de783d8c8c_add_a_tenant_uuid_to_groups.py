"""add a tenant_uuid to groups

Revision ID: c7de783d8c8c
Revises: 92928db7221

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7de783d8c8c'
down_revision = '92928db7221'

TABLE = 'groupfeatures'


def find_default_tenant_uuid():
    entity_table = sa.sql.table(
        'entity',
        sa.sql.column('id'),
        sa.sql.column('name'),
        sa.sql.column('tenant_uuid'),
    )
    query = sa.sql.select([entity_table.c.tenant_uuid]).order_by(entity_table.c.id)
    for row in op.get_bind().execute(query):
        return row.tenant_uuid


def get_context_tenant_map():
    tbl = sa.sql.table('context', sa.sql.column('name'), sa.sql.column('tenant_uuid'))
    query = sa.sql.select([tbl.c.name, tbl.c.tenant_uuid])
    rows = op.get_bind().execute(query)
    return {row.name: row.tenant_uuid for row in rows}


def associate_tenants():
    tbl = sa.sql.table(TABLE, sa.sql.column('context'), sa.sql.column('tenant_uuid'))

    for name, uuid in get_context_tenant_map().items():
        query = tbl.update().where(tbl.c.context == name).values(tenant_uuid=uuid)
        op.execute(query)


def upgrade():
    default_tenant = find_default_tenant_uuid()
    op.add_column(
        TABLE,
        sa.Column(
            'tenant_uuid',
            sa.String(36),
            sa.ForeignKey('tenant.uuid', ondelete='CASCADE'),
            nullable=False,
            server_default=default_tenant),
    )
    associate_tenants()
    op.alter_column(TABLE, 'tenant_uuid', server_default=None)


def downgrade():
    op.drop_column(TABLE, 'tenant_uuid')
