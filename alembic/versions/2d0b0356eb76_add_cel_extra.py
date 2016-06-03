"""add cel extra

Revision ID: 2d0b0356eb76
Revises: 3ecc983a901c

"""

# revision identifiers, used by Alembic.
revision = '2d0b0356eb76'
down_revision = '3ecc983a901c'

from alembic import op
from sqlalchemy import Column, Text


def upgrade():
    op.add_column('cel', Column('extra', Text))


def downgrade():
    op.drop_column('cel', 'extra')
