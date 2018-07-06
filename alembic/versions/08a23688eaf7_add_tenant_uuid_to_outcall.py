"""add tenant_uuid to outcall

Revision ID: 08a23688eaf7
Revises: 5f8c8a323cbe

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08a23688eaf7'
down_revision = '5f8c8a323cbe'

TBL = 'outcall'


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


def associate_tenants():
    ctx_tbl = sa.sql.table('context', sa.sql.column('name'), sa.sql.column('tenant_uuid'))
    outcall_tbl = sa.sql.table('outcall', sa.sql.column('context'), sa.sql.column('tenant_uuid'))
    query = sa.sql.select([ctx_tbl.c.name, ctx_tbl.c.tenant_uuid])
    context_to_tenant = {row.name: row.tenant_uuid for row in op.get_bind().execute(query)}

    for name, tenant_uuid in context_to_tenant.iteritems():
        query = outcall_tbl.update().where(outcall_tbl.c.context == name).values(tenant_uuid=tenant_uuid)
        op.execute(query)


def upgrade():
    default_tenant_uuid = find_default_tenant_uuid()
    op.add_column(
        TBL,
        sa.Column(
            'tenant_uuid',
            sa.String(36),
            sa.ForeignKey('tenant.uuid', ondelete='CASCADE'),
            nullable=False,
            server_default=default_tenant_uuid,
        )
    )
    associate_tenants()
    op.alter_column(TBL, 'tenant_uuid', server_default=None)


def downgrade():
    op.drop_column(TBL, 'tenant_uuid')
