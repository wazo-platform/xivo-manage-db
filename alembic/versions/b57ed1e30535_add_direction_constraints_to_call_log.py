"""add_direction_constraints_to_call_log

Revision ID: b57ed1e30535
Revises: 29a5eab6a19b

"""

# revision identifiers, used by Alembic.
revision = 'b57ed1e30535'
down_revision = '29a5eab6a19b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_check_constraint('call_log_direction_check',
                               'call_log',
                               sa.sql.column('direction').in_(['inbound', 'internal', 'outbound']))


def downgrade():
    op.drop_constraint('call_log_direction_check', 'call_log')
