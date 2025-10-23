"""Add shared field to voicemails

Revision ID: f16fdc26c6c6
Revises: 22b03291f3ac

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = 'f16fdc26c6c6'
down_revision = '22b03291f3ac'


def upgrade():
    op.add_column('voicemail', sa.Column('shared', sa.Boolean, nullable=False, server_default=sa.text('false')))
    op.create_index('voicemail__idx__unique_shared_per_context', 'voicemail', ['shared','context'], unique=True, postgresql_where=('shared'))


def downgrade():
    op.drop_index('voicemail__idx__unique_shared_per_context', 'voicemail')
    op.drop_column('voicemail', 'shared')
