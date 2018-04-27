"""call_log: add internal extensions

Revision ID: 3a091c2f91bc
Revises: b8f8ba046d25

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a091c2f91bc'
down_revision = 'b8f8ba046d25'


def upgrade():
    op.add_column('call_log', sa.Column('source_internal_exten', sa.Text))
    op.add_column('call_log', sa.Column('source_internal_context', sa.Text))
    op.add_column('call_log', sa.Column('destination_internal_exten', sa.Text))
    op.add_column('call_log', sa.Column('destination_internal_context', sa.Text))
    op.add_column('call_log', sa.Column('requested_internal_exten', sa.Text))
    op.add_column('call_log', sa.Column('requested_internal_context', sa.Text))


def downgrade():
    op.drop_column('call_log', 'source_internal_exten')
    op.drop_column('call_log', 'source_internal_context')
    op.drop_column('call_log', 'destination_internal_exten')
    op.drop_column('call_log', 'destination_internal_context')
    op.drop_column('call_log', 'requested_internal_exten')
    op.drop_column('call_log', 'requested_internal_context')
