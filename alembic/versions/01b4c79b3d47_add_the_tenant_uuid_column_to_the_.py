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


def upgrade():
    # The dummy tenant is to be able to add a foreign key on the entity table.
    # The real relationship will be added as a post-start script.
    dummy_tenant_uuid = _create_tenant()
    op.add_column(
        'entity',
        sa.Column(
            'tenant_uuid',
            sa.String(36),
            nullable=False,
            server_default=dummy_tenant_uuid,
            sa.ForeignKey='tenant.uuid',
        ),
    )

    op.alter_column('entity', 'tenant_uuid', server_default=None)


def downgrade():
    op.drop_constraint('user_tenant_fk', 'entity', type_='foreignkey')
    op.drop_column('entity', 'tenant_uuid')
