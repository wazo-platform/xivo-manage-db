"""trunk_add_tenant_uuid

Revision ID: 5a285558e46e
Revises: ee27cd6ccd9

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a285558e46e'
down_revision = 'ee27cd6ccd9'

TABLE = 'trunkfeatures'


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
    tbl = sa.sql.table('trunkfeatures', sa.sql.column('id'), sa.sql.column('tenant_uuid'))
    sql = "SELECT trunkfeatures.id, context.tenant_uuid FROM trunkfeatures, context WHERE trunkfeatures.context = context.name"
    trunkfeatures_to_tenant = op.get_bind().execute(sa.sql.text(sql))

    for trunkfeatures_id, tenant_uuid in trunkfeatures_to_tenant:
        query = tbl.update().where(tbl.c.id == trunkfeatures_id).values(tenant_uuid=tenant_uuid)
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
