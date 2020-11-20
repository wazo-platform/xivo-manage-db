"""add_deleted_col_to_stat_tables

Revision ID: 2f354a1653fc
Revises: b1c4be6f46ff

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '2f354a1653fc'
down_revision = 'b1c4be6f46ff'


def upgrade():
    op.add_column(
        'stat_queue',
        sa.Column('deleted', sa.Boolean, nullable=False, server_default='false'),
    )
    op.add_column(
        'stat_agent',
        sa.Column('deleted', sa.Boolean, nullable=False, server_default='false'),
    )


def downgrade():
    op.drop_column('stat_agent', 'deleted')
    op.drop_column('stat_queue', 'deleted')
