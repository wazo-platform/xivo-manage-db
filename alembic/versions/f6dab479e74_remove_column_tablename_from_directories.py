"""remove column tablename from directories

Revision ID: f6dab479e74
Revises: 2acff5c02871

"""

# revision identifiers, used by Alembic.
revision = 'f6dab479e74'
down_revision = '2acff5c02871'

from alembic import op
import sqlalchemy as sa

TABLE = 'directories'
COLUMN = 'tablename'


def upgrade():
    op.drop_column(TABLE, COLUMN)


def downgrade():
    op.add_column(TABLE, sa.Column(COLUMN, sa.String(255)))
