"""usercustom_add_tenant_uuid

Revision ID: 41b6afe5b164
Revises: 354fe6b9e819

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41b6afe5b164'
down_revision = '354fe6b9e819'

TABLE = 'usercustom'


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
    tbl = sa.sql.table('usercustom', sa.sql.column('id'), sa.sql.column('tenant_uuid'))
    sql = "SELECT usercustom.id, context.tenant_uuid FROM usercustom JOIN linefeatures ON (linefeatures.protocol = 'custom' AND linefeatures.protocolid = usercustom.id) JOIN context ON linefeatures.context = context.name"
    usercustom_to_tenant = op.get_bind().execute(sa.sql.text(sql))

    for usercustom_id, tenant_uuid in usercustom_to_tenant:
        query = tbl.update().where(tbl.c.id == usercustom_id).values(tenant_uuid=tenant_uuid)
        op.execute(query)

    sql = "SELECT usercustom.id, trunkfeatures.tenant_uuid FROM usercustom, trunkfeatures WHERE trunkfeatures.protocol = 'custom' AND trunkfeatures.protocolid = usercustom.id"
    usercustom_to_tenant = op.get_bind().execute(sa.sql.text(sql))

    for usercustom_id, tenant_uuid in usercustom_to_tenant:
        query = tbl.update().where(tbl.c.id == usercustom_id).values(tenant_uuid=tenant_uuid)
        op.execute(query)

    sql = "SELECT usercustom.id, context.tenant_uuid FROM usercustom JOIN context ON usercustom.context = context.name LEFT JOIN linefeatures ON (linefeatures.protocol = 'custom' AND linefeatures.protocolid = usercustom.id) LEFT JOIN trunkfeatures ON (trunkfeatures.protocol = 'custom' AND trunkfeatures.protocolid = usercustom.id) WHERE linefeatures.protocolid IS NULL AND trunkfeatures.protocolid IS NULL;"
    usercustom_to_tenant = op.get_bind().execute(sa.sql.text(sql))

    for usercustom_id, tenant_uuid in usercustom_to_tenant:
        query = tbl.update().where(tbl.c.id == usercustom_id).values(tenant_uuid=tenant_uuid)
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
