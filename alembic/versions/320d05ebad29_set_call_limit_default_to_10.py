"""set call limit default to 10

Revision ID: 320d05ebad29
Revises: 20d4630f2c8e

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = '320d05ebad29'
down_revision = '20d4630f2c8e'


def upgrade():
    op.alter_column("usersip", "call-limit", server_default="10")


def downgrade():
    op.alter_column("usersip", "call-limit", server_default="0")
