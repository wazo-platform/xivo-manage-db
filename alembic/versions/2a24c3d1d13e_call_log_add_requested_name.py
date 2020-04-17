"""call_log_add_requested_name

Revision ID: 2a24c3d1d13e
Revises: 4d736bac41cb

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a24c3d1d13e'
down_revision = '4d736bac41cb'


def upgrade():
    op.add_column('call_log', sa.Column('requested_name', sa.Text))


def downgrade():
    op.drop_column('call_log', 'requested_name')
