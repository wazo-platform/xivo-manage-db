"""remove exchange voicemail

Revision ID: 30d59d9b4b6e
Revises: 3b7b334edb5c

"""

# revision identifiers, used by Alembic.
revision = '30d59d9b4b6e'
down_revision = '3b7b334edb5c'

from alembic import op

from sqlalchemy.types import Integer, String
from sqlalchemy.schema import Column


def upgrade():
    op.drop_column('general', 'exchange_trunkid')
    op.drop_column('general', 'exchange_exten')


def downgrade():
    op.add_column('general', Column('exchange_trunkid', Integer))
    op.add_column('general', Column('exchange_exten', String(128)))
