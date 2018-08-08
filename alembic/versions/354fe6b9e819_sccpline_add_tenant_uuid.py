"""sccpline_add_tenant_uuid

Revision ID: 354fe6b9e819
Revises: 4a0281e1a826

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '354fe6b9e819'
down_revision = '4a0281e1a826'

TABLE = 'sccpline'


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
    tbl = sa.sql.table('sccpline', sa.sql.column('id'), sa.sql.column('tenant_uuid'))
    sql = "SELECT sccpline.id, context.tenant_uuid FROM sccpline JOIN linefeatures ON (linefeatures.protocol = 'sccp' AND linefeatures.protocolid = sccpline.id) JOIN context ON linefeatures.context = context.name"
    sccpline_to_tenant = op.get_bind().execute(sa.sql.text(sql))

    for sccpline_id, tenant_uuid in sccpline_to_tenant:
        query = tbl.update().where(tbl.c.id == sccpline_id).values(tenant_uuid=tenant_uuid)
        op.execute(query)

    sql = "SELECT sccpline.id, context.tenant_uuid FROM sccpline JOIN context ON sccpline.context = context.name LEFT JOIN linefeatures ON (linefeatures.protocol = 'sccp' AND linefeatures.protocolid = sccpline.id) WHERE linefeatures.protocolid IS NULL"
    sccpline_to_tenant = op.get_bind().execute(sa.sql.text(sql))

    for sccpline_id, tenant_uuid in sccpline_to_tenant:
        query = tbl.update().where(tbl.c.id == sccpline_id).values(tenant_uuid=tenant_uuid)
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
