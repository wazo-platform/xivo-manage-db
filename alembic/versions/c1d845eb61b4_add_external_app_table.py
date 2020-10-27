"""add_external_app_table

Revision ID: c1d845eb61b4
Revises: f207de52e7d0

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1d845eb61b4'
down_revision = 'f207de52e7d0'


def upgrade():
    op.create_table(
        'external_app',
        sa.Column('name', sa.Text, primary_key=True),
        sa.Column(
            'tenant_uuid',
            sa.String(36),
            sa.ForeignKey('tenant.uuid', ondelete='CASCADE'),
            primary_key=True
        ),
        sa.Column('label', sa.Text),
        sa.Column('configuration', sa.JSON),
    )


def downgrade():
    op.drop_table('external_app')
