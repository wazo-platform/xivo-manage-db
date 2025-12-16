"""Rename voicemails shared field to global

Revision ID: 2e24743c7a1a
Revises: f16fdc26c6c6

"""

import sqlalchemy as sa

from alembic import op
from sqlalchemy.sql import text


# revision identifiers, used by Alembic.
revision = '2e24743c7a1a'
down_revision = 'f16fdc26c6c6'


def upgrade():
    op.drop_index('voicemail__idx__unique_shared_per_context', 'voicemail')
    op.alter_column('voicemail', 'shared', new_column_name='global', nullable=False)
    op.create_index('voicemail__idx__unique_global_per_context', 'voicemail', ['global','context'], unique=True, postgresql_where=(text('global is true')))


def downgrade():
    op.drop_index('voicemail__idx__unique_global_per_context', 'voicemail')
    op.alter_column('voicemail', 'global', new_column_name='shared', nullable=False)
    op.create_index('voicemail__idx__unique_shared_per_context', 'voicemail', ['shared','context'], unique=True, postgresql_where=(text('shared is true')))
