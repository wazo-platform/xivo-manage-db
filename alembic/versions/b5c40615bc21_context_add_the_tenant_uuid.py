"""context: add the tenant_uuid

Revision ID: b5c40615bc21
Revises: 378c46e8c6fe

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b5c40615bc21'
down_revision = '378c46e8c6fe'

entity_table = sa.sql.table(
    'entity',
    sa.sql.column('name'),
    sa.sql.column('tenant_uuid'),
)


def associate_tenants(default_tenant):
    tbl = sa.sql.table('context', sa.sql.column('entity'), sa.sql.column('tenant_uuid'))

    query = tbl.update().values(tenant_uuid=default_tenant)
    op.execute(query)

    for name, uuid in get_entity_tenant_map().iteritems():
        query = tbl.update().where(tbl.c.entity == name).values(tenant_uuid=uuid)
        op.execute(query)

    query = tbl.delete().where(tbl.c.tenant_uuid == None)
    op.execte(query)


def get_entity_tenant_map():
    query = sa.sql.select([entity_table.c.name, entity_table.c.tenant_uuid])
    rows = op.get_bind().execute(query)
    return {row.name: row.tenant_uuid for row in rows}


def find_default_tenant_uuid():
    query = sa.sql.select([entity_table.c.tenant_uuid])
    for row in op.get_bind().execute(query):
        return row.tenant_uuid


def upgrade():
    op.add_column(
        'context',
        sa.Column('tenant_uuid', sa.String(36), sa.ForeignKey('tenant.uuid'), nullable=True),
    )
    default_tenant = find_default_tenant_uuid()
    associate_tenants(default_tenant)
    op.alter_column('context', 'tenant_uuid', nullable=False)


def downgrade():
    op.drop_column('context', 'tenant_uuid')
