"""remove moh unique name constraint

Revision ID: f148a8e97b74
Revises: da06cfd76289
b
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f148a8e97b74'
down_revision = 'da06cfd76289'


def upgrade():
    op.drop_constraint('moh_name_key', 'moh')


def downgrade():
    op.create_unique_constraint('moh_name_key', 'moh', ['name'])
