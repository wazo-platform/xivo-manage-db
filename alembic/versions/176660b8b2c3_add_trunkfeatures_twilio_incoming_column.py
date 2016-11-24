"""add trunkfeatures twilio_incoming column

Revision ID: 176660b8b2c3
Revises: 291ed250b7a2

"""

# revision identifiers, used by Alembic.
revision = '176660b8b2c3'
down_revision = '291ed250b7a2'

from alembic import op
from sqlalchemy import Column, Boolean


def upgrade():
    op.add_column('trunkfeatures', Column('twilio_incoming', Boolean, nullable=False, server_default='False'))


def downgrade():
    op.drop_column('trunkfeatures', 'twilio_incoming')
