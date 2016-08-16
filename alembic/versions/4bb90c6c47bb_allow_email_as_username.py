"""allow email as username

Revision ID: 4bb90c6c47bb
Revises: edb58b09b15

"""

# revision identifiers, used by Alembic.
revision = '4bb90c6c47bb'
down_revision = 'edb58b09b15'

from alembic import op
from sqlalchemy.types import String

TABLE_NAME = 'userfeatures'
NEW_TYPE = String(254)


def upgrade():
    op.alter_column(TABLE_NAME, 'email', type_=NEW_TYPE)
    op.alter_column(TABLE_NAME, 'loginclient', type_=NEW_TYPE)


def downgrade():
    op.alter_column(TABLE_NAME, 'email', type_=String(128))
    op.alter_column(TABLE_NAME, 'loginclient', type_=String(64))
