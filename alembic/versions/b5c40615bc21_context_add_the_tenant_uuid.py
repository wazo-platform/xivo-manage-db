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


def associate_tenants():
    tbl = sa.sql.table('context', sa.sql.column('entity'), sa.sql.column('tenant_uuid'))
    for name, uuid in get_entity_tenant_map().iteritems():
        query = tbl.update().where(tbl.c.entity == name).values(tenant_uuid=uuid)
        op.execute(query)


def get_entity_tenant_map():
    query = sa.sql.select([entity_table.c.name, entity_table.c.tenant_uuid])
    rows = op.get_bind().execute(query)
    return {row.name: row.tenant_uuid for row in rows}


def upgrade():
    op.add_column(
        'context',
        sa.Column('tenant_uuid', sa.String(36), sa.ForeignKey('tenant.uuid'), nullable=True),
    )
    associate_tenants()
    op.alter_column('context', 'tenant_uuid', nullable=False)


def downgrade():
    op.drop_column('context', 'tenant_uuid')
