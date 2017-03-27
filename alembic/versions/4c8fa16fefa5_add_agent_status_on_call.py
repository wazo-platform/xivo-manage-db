"""add agent status on call

Revision ID: 4c8fa16fefa5
Revises: 4e07e476eb0b

"""

# revision identifiers, used by Alembic.
revision = '4c8fa16fefa5'
down_revision = '4e07e476eb0b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('agent_login_status',
                  sa.Column('on_call', sa.Boolean, nullable=False, server_default='false'))


def downgrade():
    op.drop_column('agent_login_status', 'on_call')
