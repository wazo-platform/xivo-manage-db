"""remove-number-context-from-groupfeatures

Revision ID: e71820229900
Revises: 7f337d6ca187

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e71820229900'
down_revision = '7f337d6ca187'


def upgrade():
    op.drop_column('groupfeatures', 'number')
    op.drop_column('groupfeatures', 'context')


def downgrade():
    op.add_column('groupfeatures', sa.Column('context', sa.String(39), index=True))
    op.add_column('groupfeatures', sa.Column('number', sa.String(40), index=True))
