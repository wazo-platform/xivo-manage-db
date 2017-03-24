"""add paused and paused reason to agent status

Revision ID: 4e07e476eb0b
Revises: 19a869176d6c

"""

# revision identifiers, used by Alembic.
revision = '4e07e476eb0b'
down_revision = '19a869176d6c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('agent_login_status',
                  sa.Column('paused', sa.Boolean, nullable=False, server_default='false'))
    op.add_column('agent_login_status',
                  sa.Column('paused_reason', sa.String(256), nullable=True))


def downgrade():
    op.drop_column('agent_login_status', 'paused')
    op.drop_column('agent_login_status', 'paused_reason')
