"""remove_deleted_from_groupfeatures

Revision ID: 0b694daf27e0
Revises: e71820229900

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b694daf27e0'
down_revision = 'e71820229900'


def upgrade():
    op.drop_column('groupfeatures', 'deleted')


def downgrade():
    op.add_column(
        'groupfeatures',
        sa.Column('deleted', sa.Integer, nullable=False, server_default='0'),
    )
