"""remove_acesswebservice_acl_obj

Revision ID: 379ed6d9a62
Revises: 5524f5f02959

"""

# revision identifiers, used by Alembic.
revision = '379ed6d9a62'
down_revision = '5524f5f02959'

from alembic import op


def upgrade():
    op.drop_column('accesswebservice', 'obj')


def downgrade():
    pass
