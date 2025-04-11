"""add blocklist_number table

Revision ID: 7e13ede8dbb1
Revises: 29af79d2384d

"""

import sqlalchemy as sa

from alembic import op
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = '7e13ede8dbb1'
down_revision = '29af79d2384d'


def upgrade():
    op.create_table(
        'blocklist',
        sa.Column(
            'uuid',
            UUID,
            server_default=sa.text('uuid_generate_v4()'),
            primary_key=True,
        ),
        sa.Column(
            'tenant_uuid',
            sa.String(36),
            sa.ForeignKey('tenant.uuid', ondelete='CASCADE'),
            nullable=False,
        ),
    )
    op.create_table(
        'blocklist_number',
        sa.Column(
            'uuid',
            UUID,
            server_default=sa.text('uuid_generate_v4()'),
            primary_key=True,
        ),
        sa.Column(
            'blocklist_uuid',
            UUID,
            nullable=False,
        ),
        sa.Column('number', sa.Text, nullable=False),
        sa.Column('label', sa.Text),
    )
    op.create_table(
        'blocklist_user',
        sa.Column(
            'user_uuid',
            sa.String(36),
            nullable=False,
            primary_key=True,
        ),
        sa.Column(
            'blocklist_uuid',
            UUID,
            nullable=False,
            primary_key=True,
        ),
    )
    op.create_foreign_key(
        'blocklist_number_blocklist_uuid_fkey',
        'blocklist_number',
        'blocklist',
        ['blocklist_uuid'],
        ['uuid'],
        ondelete='CASCADE',
    )
    op.create_unique_constraint(
        'blocklist_number_number_blocklist_uuid_key',
        'blocklist_number',
        ['number', 'blocklist_uuid'],
    )
    op.create_foreign_key(
        'blocklist_user_user_uuid_fkey',
        'blocklist_user',
        'userfeatures',
        ['user_uuid'],
        ['uuid'],
        ondelete='CASCADE',
    )
    op.create_foreign_key(
        'blocklist_user_blocklist_uuid_fkey',
        'blocklist_user',
        'blocklist',
        ['blocklist_uuid'],
        ['uuid'],
        ondelete='CASCADE',
    )
    op.create_index(
        'blocklist__idx__tenant_uuid',
        'blocklist',
        ['tenant_uuid'],
    )


def downgrade():
    op.drop_table('blocklist_user')
    op.drop_table('blocklist_number')
    op.drop_table('blocklist')
