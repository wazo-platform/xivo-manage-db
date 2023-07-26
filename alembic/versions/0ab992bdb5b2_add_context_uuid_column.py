"""add context uuid column

Revision ID: 0ab992bdb5b2
Revises: 2c20d1f4ed7e

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = '0ab992bdb5b2'
down_revision = '2c20d1f4ed7e'


def upgrade():
    op.add_column(
        'context',
        sa.Column('uuid', UUID, server_default=sa.text('uuid_generate_v4()'), unique=True),
    )


def downgrade():
    op.drop_column('context', 'uuid')
