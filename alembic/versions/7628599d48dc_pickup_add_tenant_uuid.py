"""pickup_add_tenant_uuid

Revision ID: 7628599d48dc
Revises: 3f132402532b

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '7628599d48dc'
down_revision = '3f132402532b'

TABLE = 'pickup'


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
    tbl = sa.sql.table('pickup', sa.sql.column('id'), sa.sql.column('tenant_uuid'))
    sql = "SELECT pickup.id, entity.tenant_uuid FROM pickup, entity WHERE entity.id=pickup.entity_id"
    pickup_to_tenant = op.get_bind().execute(sa.sql.text(sql))

    for pickup_id, tenant_uuid in pickup_to_tenant:
        query = tbl.update().where(tbl.c.id == pickup_id).values(tenant_uuid=tenant_uuid)
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
