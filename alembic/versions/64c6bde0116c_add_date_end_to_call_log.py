"""add_date_end_to_call_log

Revision ID: 64c6bde0116c
Revises: b5f230e1e0fe

"""

# revision identifiers, used by Alembic.
revision = '64c6bde0116c'
down_revision = 'b5f230e1e0fe'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('call_log', sa.Column('date_end', sa.DateTime))


def downgrade():
    op.drop_column('call_log', 'date_end')
