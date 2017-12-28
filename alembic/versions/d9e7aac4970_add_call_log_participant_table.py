"""add call_log_participant table

Revision ID: d9e7aac4970
Revises: 42e9771685b0

"""

# revision identifiers, used by Alembic.
revision = 'd9e7aac4970'
down_revision = '42e9771685b0'

import sqlalchemy as sa
from alembic import op


def upgrade():
    op.create_table(
        'call_log_participant',
        sa.Column('uuid', sa.String(38)),
        sa.Column('call_log_id', sa.Integer),
        sa.Column('user_uuid', sa.String(38), nullable=False),
        sa.Column('line_id', sa.Integer),
        sa.Column('role', sa.Enum('source', 'destination', name='call_log_participant_role'), nullable=False),
        sa.PrimaryKeyConstraint('uuid'),
        sa.ForeignKeyConstraint(['call_log_id'], ['call_log.id'], name='fk_call_log_id', ondelete='CASCADE'),
        sa.Index('call_log_participant__idx__user_uuid', 'user_uuid')
    )


def downgrade():
    op.drop_table('call_log_participant')
    op.execute('DROP_TYPE call_log_participant_role')
