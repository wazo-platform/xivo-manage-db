"""add_tenant_uuid_to_call_log_participant

Revision ID: 5047425b0f5c
Revises: d0f74d74eb5f

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5047425b0f5c'
down_revision = 'd0f74d74eb5f'


def upgrade():
    op.add_column(
        'call_log',
        sa.Column(
            'tenant_uuid',
            sa.String(36),
            nullable=False,
            server_default='00000000-0000-0000-0000-000000000000',
        )
    )
    op.alter_column('call_log', 'tenant_uuid', server_default=None)


def downgrade():
    op.drop_column('call_log', 'tenant_uuid')
