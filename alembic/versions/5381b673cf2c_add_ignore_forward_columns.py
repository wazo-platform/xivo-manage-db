"""add ignore_forward columns

Revision ID: 5381b673cf2c
Revises: 2d0b0356eb76

"""

# revision identifiers, used by Alembic.
revision = '5381b673cf2c'
down_revision = '2d0b0356eb76'

from alembic import op
from sqlalchemy import Column, Integer

TABLE_NAMES = ['groupfeatures', 'queuefeatures']
COLUMN_NAME = 'ignore_forward'


def upgrade():
    for table_name in TABLE_NAMES:
        # on upgrade, existing queues and groups will have "ignore_forward" set to 0 (so the
        # queue/group behaviour doesn't change on upgrade), but newly created queues will have by
        # default "ignore_forward" set to 1
        op.add_column(table_name, Column(COLUMN_NAME, Integer, nullable=False, server_default='0'))
        op.alter_column(table_name, COLUMN_NAME, server_default='1')


def downgrade():
    for table_name in TABLE_NAMES:
        op.drop_column(table_name, COLUMN_NAME)
