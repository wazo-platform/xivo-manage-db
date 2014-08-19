"""add service func key arg

Revision ID: 4ce50bcf2a0e
Revises: 41d3e47edf4a
XiVO Version: <version>

"""

# revision identifiers, used by Alembic.
revision = '4ce50bcf2a0e'
down_revision = '41d3e47edf4a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('func_key_dest_service',
                  sa.Column('argument', sa.String(20), nullable=True))


def downgrade():
    op.drop_column('func_key_dest_service', 'argument')
