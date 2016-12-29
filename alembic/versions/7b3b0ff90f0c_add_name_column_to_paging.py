"""add_name_column_to_paging

Revision ID: 7b3b0ff90f0c
Revises: 8a551a46dd5d

"""

# revision identifiers, used by Alembic.
revision = '7b3b0ff90f0c'
down_revision = '8a551a46dd5d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('paging', sa.Column('name', sa.String(128)))
    op.alter_column('paging', 'timeout', server_default='30')


def downgrade():
    op.alter_column('paging', 'timeout', server_default=None)
    op.drop_column('paging', 'name')
