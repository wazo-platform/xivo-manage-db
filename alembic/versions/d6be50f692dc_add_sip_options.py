"""add sip options

Revision ID: d6be50f692dc
Revises: 5524f5f02959

"""

# revision identifiers, used by Alembic.
revision = 'd6be50f692dc'
down_revision = '5524f5f02959'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('usersip', sa.Column('options',
                                         ARRAY(sa.String, dimensions=2),
                                         nullable=False, server_default='{}'))


def downgrade():
    op.drop_column('usersip', 'options')
