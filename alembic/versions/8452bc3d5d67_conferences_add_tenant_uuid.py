"""conferences add tenant_uuid

Revision ID: 8452bc3d5d67
Revises: 08a23688eaf7

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8452bc3d5d67'
down_revision = '08a23688eaf7'

TABLE = 'conference'


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
    tbl = sa.sql.table('conference', sa.sql.column('id'), sa.sql.column('tenant_uuid'))
    sql = "SELECT conference.id, context.tenant_uuid FROM conference, extensions, context WHERE extensions.type='conference' AND extensions.typeval=CAST(conference.id AS text) AND extensions.context = context.name"
    conference_to_tenant = op.get_bind().execute(sa.sql.text(sql))

    for conference_id, tenant_uuid in conference_to_tenant:
        query = tbl.update().where(tbl.c.id == conference_id).values(tenant_uuid=tenant_uuid)
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
