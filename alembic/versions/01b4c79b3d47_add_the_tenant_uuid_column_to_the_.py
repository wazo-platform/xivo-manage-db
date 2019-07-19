"""add the tenant_uuid column to the entity table

Revision ID: 01b4c79b3d47
Revises: 3b2e82f0bfbe

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01b4c79b3d47'
down_revision = '3b2e82f0bfbe'

tenant_table = sa.sql.table('tenant', sa.sql.column('uuid'))


def _create_tenant():
    insert_query = tenant_table.insert().returning(tenant_table.c.uuid)
    return op.get_bind().execute(insert_query).scalar()


def associate_tenants():
    tbl = sa.sql.table('entity', sa.sql.column('id'), sa.sql.column('tenant_uuid'))
    sql = "SELECT entity.id FROM entity"
    entities = op.get_bind().execute(sa.sql.text(sql))

    for entity in entities:
        # The real wazo-auth tenant will be created as a post-start script.
        tenant_uuid = _create_tenant()
        query = tbl.update().where(tbl.c.id == entity.id).values(tenant_uuid=tenant_uuid)
        op.execute(query)


def upgrade():
    op.add_column(
        'entity',
        sa.Column(
            'tenant_uuid',
            sa.String(36),
            sa.ForeignKey('tenant.uuid'),
            nullable=True,
        ),
    )
    associate_tenants()
    op.alter_column('entity', 'tenant_uuid', nullable=False)


def downgrade():
    op.drop_column('entity', 'tenant_uuid')
