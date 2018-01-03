"""add_iax_options

Revision ID: 505c12d2ed73
Revises: 672a6918b7f9

"""

# revision identifiers, used by Alembic.
revision = '505c12d2ed73'
down_revision = '672a6918b7f9'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ARRAY


def upgrade():
    op.add_column('useriax', sa.Column('options',
                                       ARRAY(sa.String, dimensions=2),
                                       nullable=False, server_default='{}'))


def downgrade():
    op.drop_column('useriax', 'options')
