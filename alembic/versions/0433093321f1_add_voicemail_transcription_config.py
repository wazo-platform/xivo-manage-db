"""add voicemail transcription config

Revision ID: 0433093321f1
Revises: 517d371081d0

"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.sql import text

# revision identifiers, used by Alembic.
revision = '0433093321f1'
down_revision = '517d371081d0'

COLUMN = 'voicemail_transcription_enabled'


def upgrade():
    op.add_column(
        'tenant',
        sa.Column(COLUMN, sa.Boolean(), nullable=False, server_default=text('false')),
    )


def downgrade():
    op.drop_column('tenant', COLUMN)
