"""add call-log requested exten

Revision ID: 36516503ae1b
Revises: 5085447dd295

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36516503ae1b'
down_revision = '5085447dd295'


def upgrade():
    op.add_column('call_log', sa.Column('requested_exten', sa.String(255)))
    op.add_column('call_log', sa.Column('requested_context', sa.String(255)))


def downgrade():
    op.drop_column('call_log', 'requested_exten')
    op.drop_column('call_log', 'requested_context')
