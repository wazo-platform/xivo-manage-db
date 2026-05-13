"""add stat_queue_id to stat_agent_periodic

Revision ID: 091ab2e3ff4d
Revises: 8863a45bcbd0

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = '091ab2e3ff4d'
down_revision = '8863a45bcbd0'


def upgrade():
    op.add_column(
        'stat_agent_periodic',
        sa.Column('stat_queue_id', sa.Integer, sa.ForeignKey('stat_queue.id'), nullable=True),
    )
    op.create_index(
        'stat_agent_periodic__idx__stat_queue_id',
        'stat_agent_periodic',
        ['stat_queue_id'],
    )


def downgrade():
    op.drop_index('stat_agent_periodic__idx__stat_queue_id', 'stat_agent_periodic')
    op.drop_column('stat_agent_periodic', 'stat_queue_id')
