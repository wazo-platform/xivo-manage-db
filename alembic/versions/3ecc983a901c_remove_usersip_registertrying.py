"""remove usersip registertrying

Revision ID: 3ecc983a901c
Revises: b8d0848e7b2

"""

# revision identifiers, used by Alembic.
revision = '3ecc983a901c'
down_revision = 'b8d0848e7b2'

from alembic import op
from sqlalchemy import Column, Integer


def upgrade():
    op.drop_column('usersip', 'registertrying')


def downgrade():
    op.add_column('usersip', Column('registertrying', Integer))
