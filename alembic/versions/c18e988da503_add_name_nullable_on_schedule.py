"""add_name_nullable_on_schedule

Revision ID: c18e988da503
Revises: 1cc52186eb47

"""

# revision identifiers, used by Alembic.
revision = 'c18e988da503'
down_revision = '1cc52186eb47'

from alembic import op


def upgrade():
    op.alter_column('schedule', 'name', nullable=True, server_default=False)


def downgrade():
    op.alter_column('schedule', 'name', nullable=False, server_default='')
