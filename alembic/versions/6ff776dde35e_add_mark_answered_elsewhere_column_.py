"""add mark_answered_elsewhere column groupfeatures queuefeatures

Revision ID: 6ff776dde35e
Revises: 108f435e1af2

"""

from alembic import op
from sqlalchemy import Column, Integer


# revision identifiers, used by Alembic.
revision = '6ff776dde35e'
down_revision = '108f435e1af2'

COLUMN_NAME = 'mark_answered_elsewhere'


def upgrade():
    # on upgrade, existing queues and groups will have "mark_answered_elsewhere" set to 0 (so
    # the queue/group behaviour doesn't change on upgrade), but newly created queues will have
    # by default "mark_answered_elsewhere" set to 1
    op.add_column('groupfeatures', Column(COLUMN_NAME, Integer, nullable=False, server_default='0'))
    op.add_column('queuefeatures', Column(COLUMN_NAME, Integer, nullable=False, server_default='0'))
    op.alter_column('queuefeatures', COLUMN_NAME, server_default='1')


def downgrade():
    op.drop_column('groupfeatures', COLUMN_NAME)
    op.drop_column('queuefeatures', COLUMN_NAME)
