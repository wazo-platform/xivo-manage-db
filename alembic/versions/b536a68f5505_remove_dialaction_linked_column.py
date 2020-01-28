"""remove-dialaction-linked-column

Revision ID: b536a68f5505
Revises: 92061fe1c3b8

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'b536a68f5505'
down_revision = '92061fe1c3b8'


def upgrade():
    op.drop_column('dialaction', 'linked')


def downgrade():
    op.add_column(
        'dialaction',
        sa.Column('linked', sa.Integer, nullable=False, server_default='0'),
    )
