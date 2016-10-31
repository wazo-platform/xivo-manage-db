"""drop column useenum

Revision ID: a132daff54b
Revises: 9142f0403c8

"""

# revision identifiers, used by Alembic.
revision = 'a132daff54b'
down_revision = '9142f0403c8'

from alembic import op
from sqlalchemy import Column, Integer


def upgrade():
    op.drop_column('outcall', 'useenum')


def downgrade():
    op.add_column('outcall', Column('useenum', Integer, nullable=False, server_default='0'))
