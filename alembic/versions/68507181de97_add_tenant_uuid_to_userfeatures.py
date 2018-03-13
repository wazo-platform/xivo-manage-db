"""add tenant_uuid to userfeatures

Revision ID: 68507181de97
Revises: 3462497a56f8

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68507181de97'
down_revision = '3462497a56f8'

tenant_table = sa.sql.table('tenant', sa.sql.column('uuid'))

def _create_tenant():
    insert_query = tenant_table.insert().returning(tenant_table.c.uuid)
    return op.get_bind().execute(insert_query).scalar()


def upgrade():
    # The dummy tenant is to be able to add a foreign key on the userfeatures table.
    # The real relationship will be added as a post-start script.
    dummy_tenant_uuid = _create_tenant()
    op.add_column(
        'userfeatures',
        sa.Column('tenant_uuid', sa.String(38), nullable=False, server_default=dummy_tenant_uuid),
    )

    op.alter_column('userfeatures', 'tenant_uuid', server_default=None)
    op.create_foreign_key(
        'user_tenant_fk',
        'userfeatures',
        'tenant',
        ['tenant_uuid'],
        ['uuid'],
    )


def downgrade():
    op.drop_constraint('user_tenant_fk', 'userfeatures', type_='foreignkey')
    op.drop_column('userfeatures', 'tenant_uuid')
