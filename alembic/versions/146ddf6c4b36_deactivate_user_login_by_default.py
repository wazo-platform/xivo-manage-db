"""deactivate user login by default

Revision ID: 146ddf6c4b36
Revises: 108164f6117e
Create Date: 2014-05-09 13:51:05.052676
XiVO Version: 14.07

"""

# revision identifiers, used by Alembic.
revision = '146ddf6c4b36'
down_revision = '108164f6117e'

from alembic import op


def upgrade():
    op.alter_column('userfeatures', 'enableclient', server_default='0')


def downgrade():
    op.alter_column('userfeatures', 'enableclient', server_default='1')
