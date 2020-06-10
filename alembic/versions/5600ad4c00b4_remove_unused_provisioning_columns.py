"""remove-unused-provisioning-columns

Revision ID: 5600ad4c00b4
Revises: d47f295009dd

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5600ad4c00b4'
down_revision = 'd47f295009dd'


def upgrade():
    op.drop_column('provisioning', 'net4_ip_rest')
    op.drop_column('provisioning', 'rest_port')


def downgrade():
    op.add_column('provisoning', sa.Column('net4_ip_rest', sa.String(39)))
    op.add_column('provisoning', sa.Column('rest_port', sa.Integer, nullable=False))
