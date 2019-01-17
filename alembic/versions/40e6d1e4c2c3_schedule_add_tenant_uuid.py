"""schedule_add_tenant_uuid

Revision ID: 40e6d1e4c2c3
Revises: 58cd88054523

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40e6d1e4c2c3'
down_revision = '58cd88054523'


TABLE = 'schedule'


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
    tbl = sa.sql.table('schedule', sa.sql.column('id'), sa.sql.column('tenant_uuid'))
    sql = "SELECT schedule.id, entity.tenant_uuid FROM schedule, entity WHERE entity.id=schedule.entity_id"
    schedule_to_tenant = op.get_bind().execute(sa.sql.text(sql))

    for schedule_id, tenant_uuid in schedule_to_tenant:
        query = tbl.update().where(tbl.c.id == schedule_id).values(tenant_uuid=tenant_uuid)
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
