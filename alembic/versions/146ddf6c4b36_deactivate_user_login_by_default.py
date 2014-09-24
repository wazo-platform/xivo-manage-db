"""deactivate user login by default

Revision ID: 146ddf6c4b36
Revises: 108164f6117e

"""

# revision identifiers, used by Alembic.
revision = '146ddf6c4b36'
down_revision = '108164f6117e'

from alembic import op


def upgrade():
    op.alter_column('userfeatures', 'enableclient', server_default='0')


def downgrade():
    op.alter_column('userfeatures', 'enableclient', server_default='1')
