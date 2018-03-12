"""add the tenant table

Revision ID: 3b2e82f0bfbe
Revises: 404300b7c16d

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b2e82f0bfbe'
down_revision = '404300b7c16d'


def upgrade():
    op.create_table(
        'tenant',
        sa.Column('uuid', sa.String(38), server_default=sa.text('uuid_generate_v4()'), primary_key=True),
    )


def downgrade():
    op.drop_table('tenant')
