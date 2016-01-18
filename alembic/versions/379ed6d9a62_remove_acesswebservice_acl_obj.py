"""remove_acesswebservice_acl_obj

Revision ID: 379ed6d9a62
Revises: d6be50f692dc

"""

# revision identifiers, used by Alembic.
revision = '379ed6d9a62'
down_revision = 'd6be50f692dc'

from alembic import op


def upgrade():
    op.drop_column('accesswebservice', 'obj')


def downgrade():
    pass
