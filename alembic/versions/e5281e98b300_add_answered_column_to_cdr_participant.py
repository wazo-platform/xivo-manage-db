"""add-answered-column-to-cdr-participant

Revision ID: e5281e98b300
Revises: 53ad771ac875

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'e5281e98b300'
down_revision = '53ad771ac875'


def upgrade():
    op.add_column(
        'call_log_participant',
        sa.Column('answered', sa.Boolean, nullable=False, server_default='false'),
    )


def downgrade():
    op.drop_column('call_log_participant', 'answered')
