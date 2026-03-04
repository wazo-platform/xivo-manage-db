"""add voicemail transcription config

Revision ID: 0433093321f1
Revises: 517d371081d0

"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql import text

# revision identifiers, used by Alembic.
revision = '0433093321f1'
down_revision = '517d371081d0'

TABLE = 'voicemail_transcription_config'


def upgrade():
    op.create_table(
        TABLE,
        sa.Column(
            'uuid',
            postgresql.UUID(as_uuid=True),
            server_default=text('uuid_generate_v4()'),
            nullable=False,
        ),
        sa.Column('tenant_uuid', sa.String(36), nullable=False),
        sa.Column(
            'enabled', sa.Boolean(), nullable=False, server_default=text('false')
        ),
        sa.PrimaryKeyConstraint('uuid'),
        sa.ForeignKeyConstraint(
            ['tenant_uuid'],
            ['tenant.uuid'],
            ondelete='CASCADE',
        ),
        sa.UniqueConstraint('tenant_uuid'),
    )

    # Populate default config for all existing tenants
    op.execute(text(f'INSERT INTO {TABLE} (tenant_uuid) SELECT uuid FROM tenant'))


def downgrade():
    op.drop_table(TABLE)
