"""drop usersip setvar column

Revision ID: 1b6be5d5e4ac
Revises: 255de5d2adea

"""

# revision identifiers, used by Alembic.
revision = '1b6be5d5e4ac'
down_revision = '255de5d2adea'

from alembic import op
from sqlalchemy.schema import Column
from sqlalchemy.types import String


def upgrade():
    op.drop_column('usersip', 'setvar')


def downgrade():
    op.add_column('usersip', Column('setvar', String(100), nullable=False, server_default=''))
