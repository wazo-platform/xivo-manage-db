"""drop_accesswebservice_table

Revision ID: 71c41130380e
Revises: 117b51a2d937

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = '71c41130380e'
down_revision = '117b51a2d937'


def upgrade():
    op.drop_table('accesswebservice')


def downgrade():
    pass
