"""Remove queue_info table.

Revision ID: 203129d6b213
Revises: 5ffaec7e8db7

"""

from alembic import op
from sqlalchemy import Column, Integer, String


# revision identifiers, used by Alembic.
revision = '203129d6b213'
down_revision = '5ffaec7e8db7'


def upgrade():
    op.drop_index('queue_info_call_time_t_index')
    op.drop_index('queue_info_queue_name_index')
    op.drop_table('queue_info')


def downgrade():
    op.create_table(
        'queue_info',
        Column('id', Integer, primary_key=True),
        Column('call_time_t', Integer),
        Column('queue_name', String(128), nullable=False, server_default=''),
        Column('caller', String(80), nullable=False, server_default=''),
        Column('caller_uniqueid', String(32), nullable=False, server_default=''),
        Column('call_picker', String(80)),
        Column('hold_time', Integer),
        Column('talk_time', Integer),
    )

    op.create_index('queue_info_call_time_t_index', 'queue_info', ['call_time_t'])
    op.create_index('queue_info_queue_name_index', 'queue_info', ['queue_name'])
