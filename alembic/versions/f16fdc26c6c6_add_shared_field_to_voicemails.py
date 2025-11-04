"""Add shared field to voicemails

Revision ID: f16fdc26c6c6
Revises: 040b55af6f67

"""

import sqlalchemy as sa

from alembic import op
from sqlalchemy.sql import text


# revision identifiers, used by Alembic.
revision = 'f16fdc26c6c6'
down_revision = '040b55af6f67'


def upgrade():
    op.add_column('voicemail', sa.Column('shared', sa.Boolean, nullable=False, server_default=text('false')))
    op.create_index('voicemail__idx__unique_shared_per_context', 'voicemail', ['shared','context'], unique=True, postgresql_where=(text('shared is true')))


def downgrade():
    op.drop_index('voicemail__idx__unique_shared_per_context', 'voicemail')
    op.drop_column('voicemail', 'shared')
