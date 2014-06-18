"""add_index_on_callid_in_stat_call_on_queue

Revision ID: 3c14d64c95a3
Revises: 37c6976343d4
Create Date: 2014-06-17 10:40:16.512779
XiVO Version: 14.11

"""

# revision identifiers, used by Alembic.
revision = '3c14d64c95a3'
down_revision = '37c6976343d4'

from alembic import op


def upgrade():
    op.create_index('stat_call_on_queue__idx_callid', 'stat_call_on_queue', ['callid'])


def downgrade():
    op.drop_index('stat_call_on_queue__idx_callid')
