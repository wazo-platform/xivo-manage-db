"""provisioning: add http base url column

Revision ID: 8005d5787610
Revises: 43b515cb6968

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8005d5787610'
down_revision = '43b515cb6968'


def upgrade():
    op.add_column('provisioning', sa.Column('http_base_url', sa.String(255)))


def downgrade():
    op.drop_column('provisioning', 'http_base_url')
