"""alter queueskill drop printscreen

Revision ID: 30f88b362201
Revises: 31eecc16c5c5

"""

# revision identifiers, used by Alembic.
revision = '30f88b362201'
down_revision = '31eecc16c5c5'

from alembic import op
from sqlalchemy.schema import Column
from sqlalchemy.types import String


def upgrade():
    op.drop_column('queueskill', 'printscreen')


def downgrade():
    op.add_column('queueskill', Column('printscreen', String(5)))
