"""add stat_switchboard_queue table

Revision ID: 53ce4ff6ffe9
Revises: 4123465e114e

"""

# revision identifiers, used by Alembic.
revision = '53ce4ff6ffe9'
down_revision = '4123465e114e'

from alembic import op
import sqlalchemy as sa


stat_switchboard_endtype = sa.Enum(
    'abandoned',
    'completed',
    'forwarded',
    'transferred',
    name='stat_switchboard_endtype',
)


def upgrade():
    op.create_table(
        'stat_switchboard_queue',
        sa.Column('id', sa.Integer, nullable=False),
        sa.Column('time', sa.DateTime, nullable=False),
        sa.Column('end_type', stat_switchboard_endtype, nullable=False),
        sa.Column('wait_time', sa.Float, nullable=False),
        sa.Column('queue_id', sa.Integer, nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(('queue_id',), ('queuefeatures.id',), ondelete='CASCADE'),
        sa.Index('stat_switchboard_queue__idx__queue_id', 'queue_id'),
        sa.Index('stat_switchboard_queue__idx__time', 'time'),
    )


def downgrade():
    op.drop_table('stat_switchboard_queue')
    stat_switchboard_endtype.drop(op.get_bind())
