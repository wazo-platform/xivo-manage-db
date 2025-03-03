"""add recording announcements to tenant

Revision ID: ba4c449afc9a
Revises: 9485e1dae58c

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = 'ba4c449afc9a'
down_revision = '9485e1dae58c'


def upgrade():
    op.add_column(
        'tenant',
        sa.Column(
            'record_start_announcement',
            sa.Text,
            nullable=True,
        ),
    )
    op.add_column(
        'tenant',
        sa.Column(
            'record_stop_announcement',
            sa.Text,
            nullable=True,
        ),
    )


def downgrade():
    op.drop_column('tenant', 'record_start_announcement')
    op.drop_column('tenant', 'record_stop_announcement')
