"""add-timezone-on-call-center-stats

Revision ID: e5e53b7dc5d0
Revises: 5497199c082f

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'e5e53b7dc5d0'
down_revision = '5497199c082f'


def upgrade():
    op.alter_column('stat_agent_periodic', 'time', type_=sa.DateTime(timezone=True))
    op.alter_column('stat_queue_periodic', 'time', type_=sa.DateTime(timezone=True))
    op.alter_column('stat_call_on_queue', 'time', type_=sa.DateTime(timezone=True))
    op.alter_column('queue_log', 'time', server_default=None, nullable=True)
    op.alter_column(
        'queue_log',
        'time',
        type_=sa.DateTime(timezone=True),
        postgresql_using='"time"::timestamp with time zone',
    )

    # NOTE(fblackburn): fix column to match asterisk recommends
    op.alter_column(
        'queue_log',
        'callid',
        type_=sa.String(80),
        server_default=None,
        nullable=True,
    )
    op.alter_column(
        'queue_log',
        'queuename',
        type_=sa.String(256),
        server_default=None,
        nullable=True
    )
    op.alter_column('queue_log', 'agent', server_default=None, nullable=True)
    op.alter_column('queue_log', 'event', server_default=None, nullable=True)
    op.alter_column('queue_log', 'data1', server_default=None)
    op.alter_column('queue_log', 'data2', server_default=None)
    op.alter_column('queue_log', 'data3', server_default=None)
    op.alter_column('queue_log', 'data4', server_default=None)
    op.alter_column('queue_log', 'data5', server_default=None)


def downgrade():
    op.alter_column('queue_log', 'data5', server_default='')
    op.alter_column('queue_log', 'data4', server_default='')
    op.alter_column('queue_log', 'data3', server_default='')
    op.alter_column('queue_log', 'data2', server_default='')
    op.alter_column('queue_log', 'data1', server_default='')
    op.alter_column('queue_log', 'event', server_default='', nullable=False)
    op.alter_column('queue_log', 'agent', server_default='', nullable=False)
    op.alter_column(
        'queue_log',
        'queuename',
        type_=sa.String(50),
        server_default='',
        nullable=False,
    )
    op.alter_column(
        'queue_log',
        'callid',
        type_=sa.String(32),
        server_default='',
        nullable=False,
    )
    op.alter_column('queue_log', 'time', type_=sa.String(80))
    op.alter_column('queue_log', 'time', server_default='', nullable=False)
    op.alter_column('stat_call_on_queue', 'time', type_=sa.DateTime())
    op.alter_column('stat_queue_periodic', 'time', type_=sa.DateTime())
    op.alter_column('stat_agent_periodic', 'time', type_=sa.DateTime())
