"""remove unused indexes on cel and qlog tables

Revision ID: 2c6c9833d839
Revises: 30f88b362201
XiVO Version: 14.14

"""

# revision identifiers, used by Alembic.
revision = '2c6c9833d839'
down_revision = '30f88b362201'

from alembic import op


def upgrade():
    op.drop_index('cel__idx__uniqueid')
    op.drop_index('queue_log__idx_queuename')


def downgrade():
    op.create_index('cel__idx__uniqueid', 'cel', ['uniqueid'])
    op.create_index('queue_log__idx_queuename', 'queue_log', ['queuename'])
