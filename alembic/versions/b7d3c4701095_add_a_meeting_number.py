"""add a meeting number

Revision ID: b7d3c4701095
Revises: 2b51ff81d388

"""

import random

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7d3c4701095'
down_revision = '2b51ff81d388'

TABLE_NAME = 'meeting'
COLUMN_NAME = 'number'

def random_number(length=6):
    return str(random.randint(0, int('9' * length))).rjust(length, '0')


def upgrade():
    op.add_column(TABLE_NAME, sa.Column(COLUMN_NAME, sa.Text, nullable=False, default=random_number))


def downgrade():
    op.drop_column(TABLE_NAME, COLUMN_NAME)
