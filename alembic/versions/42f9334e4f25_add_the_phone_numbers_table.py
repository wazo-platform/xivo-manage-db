"""add the phone-number table

Revision ID: 42f9334e4f25
Revises: c55e390ac48c

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = '42f9334e4f25'
down_revision = 'c55e390ac48c'

TABLE_NAME = 'phone_number'


def upgrade():
    op.create_table(
        TABLE_NAME,
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
        sa.Column('number', sa.Text, nullable=False),
        sa.Column('caller_id_name', sa.Text),
        sa.Column(
            'main',
            sa.Boolean,
            nullable=False,
            server_default='false',
        ),
        sa.Column(
            'shared',
            sa.Boolean,
            nullable=False,
            server_default='false',
        ),
    )
    op.create_unique_constraint(
        f'{TABLE_NAME}_number_tenant_uuid_key',
        TABLE_NAME,
        ['number', 'tenant_uuid'],
    )
    op.create_index(
        'only_one_main_allowed',
        TABLE_NAME,
        ['main', 'tenant_uuid'],
        unique=True,
        postgresql_where=(sa.text('main is true')),
    )


def downgrade():
    op.drop_table(TABLE_NAME)
