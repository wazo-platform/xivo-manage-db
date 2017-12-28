"""add_direction_to_call_log

Revision ID: 27801f8c2a80
Revises: dba4e40979ae

"""

# revision identifiers, used by Alembic.
revision = '27801f8c2a80'
down_revision = 'dba4e40979ae'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('call_log', sa.Column('direction', sa.String(255)))


def downgrade():
    op.drop_column('call_log', 'direction')
