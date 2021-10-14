"""add meeting creation date

Revision ID: 035908ce02df
Revises: 37c0864e0b2b

"""

import datetime
import sqlalchemy as sa

from alembic import op
from sqlalchemy.types import DateTime
from sqlalchemy.schema import Column


# revision identifiers, used by Alembic.
revision = '035908ce02df'
down_revision = '035e2cb65b6d'


def upgrade():
    op.add_column('meeting', Column('created_at', DateTime(timezone=True), default=datetime.datetime.utcnow, server_default=sa.text("(now() at time zone 'utc')")))


def downgrade():
    op.drop_column('meeting', 'created_at')
