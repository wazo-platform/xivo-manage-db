"""allow-context-none-in-outcall.py

Revision ID: 4fd0315a61fc
Revises: 15b236bd8060

"""

# revision identifiers, used by Alembic.
revision = '4fd0315a61fc'
down_revision = '15b236bd8060'

from alembic import op


def upgrade():
    op.alter_column('outcall', 'context', nullable=True)


def downgrade():
    op.alter_column('outcall', 'context', nullable=False)
