"""add_dtmf_hangup_to_userfeatures

Revision ID: 333cd1b1d31
Revises: 56e683a865e0

"""

# revision identifiers, used by Alembic.
revision = '333cd1b1d31'
down_revision = '56e683a865e0'


from sqlalchemy import Column
from sqlalchemy.types import Integer
from alembic import op


def upgrade():
    op.add_column('userfeatures', Column('dtmf_hangup', Integer, nullable=False, server_default='0'))


def downgrade():
    op.drop_column('userfeatures', 'dtmf_hangup')
