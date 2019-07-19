"""add tenant_uuid to userfeatures

Revision ID: 68507181de97
Revises: 3462497a56f8

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68507181de97'
down_revision = '3462497a56f8'


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
    tbl = sa.sql.table('userfeatures', sa.sql.column('id'), sa.sql.column('tenant_uuid'))
    sql = "SELECT userfeatures.id, entity.tenant_uuid FROM userfeatures, entity WHERE entity.id=userfeatures.entityid"
    userfeatures_to_tenant = op.get_bind().execute(sa.sql.text(sql))

    for userfeatures_id, tenant_uuid in userfeatures_to_tenant:
        query = tbl.update().where(tbl.c.id == userfeatures_id).values(tenant_uuid=tenant_uuid)
        op.execute(query)


def upgrade():
    default_tenant = find_default_tenant_uuid()
    op.add_column(
        'userfeatures',
        sa.Column(
            'tenant_uuid',
            sa.String(36),
            sa.ForeignKey('tenant.uuid'),
            nullable=False,
            server_default=default_tenant,
        ),
    )
    associate_tenants()
    op.alter_column('userfeatures', 'tenant_uuid', server_default=None)


def downgrade():
    op.drop_column('userfeatures', 'tenant_uuid')
