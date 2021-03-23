"""add the tenant slug

Revision ID: 757111d049b6
Revises: 382aaefc59ec

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '757111d049b6'
down_revision = '382aaefc59ec'


def upgrade():
    op.add_column('tenant', sa.Column('slug', sa.String(10)))


def downgrade():
    op.drop_column('tenant', 'slug')
