"""adjust agent_login_status login_at

Revision ID: 3c9280e9ed5c
Revises: 2c940e077157

"""

# revision identifiers, used by Alembic.
revision = '3c9280e9ed5c'
down_revision = '2c940e077157'

from alembic import op
from sqlalchemy import text


def upgrade():
    op.execute("UPDATE agent_login_status SET login_at = cast(login_at as timestamp with time zone) at time zone 'utc'")
    op.alter_column('agent_login_status', 'login_at', server_default=text("(current_timestamp at time zone 'utc')"))


def downgrade():
    pass
