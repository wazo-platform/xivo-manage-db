"""parking_lot_add_tenant_uuid

Revision ID: 232708be8a75
Revises: 4f85f1de19b4

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '232708be8a75'
down_revision = '4f85f1de19b4'

TABLE = 'parking_lot'


def find_default_tenant_uuid():
    entity_table = sa.sql.table(
        'entity',
        sa.sql.column('id'),
        sa.sql.column('tenant_uuid'),
    )
    query = sa.sql.select([entity_table.c.tenant_uuid]).order_by(entity_table.c.id)
    for row in op.get_bind().execute(query):
        return row.tenant_uuid


def associate_tenants():
    tbl = sa.sql.table('parking_lot', sa.sql.column('id'), sa.sql.column('tenant_uuid'))
    sql = "SELECT parking_lot.id, context.tenant_uuid FROM parking_lot, extensions, context WHERE extensions.type='parking' AND extensions.typeval=CAST(parking_lot.id AS text) AND extensions.context = context.name"
    parking_lot_to_tenant = op.get_bind().execute(sa.sql.text(sql))

    for parking_lot_id, tenant_uuid in parking_lot_to_tenant:
        query = tbl.update().where(tbl.c.id == parking_lot_id).values(tenant_uuid=tenant_uuid)
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
