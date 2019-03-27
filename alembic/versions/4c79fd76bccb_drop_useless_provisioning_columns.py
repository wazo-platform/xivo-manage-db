"""drop useless provisioning columns
Revision ID: 4c79fd76bccb
Revises: a3b4e1bf633b

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c79fd76bccb'
down_revision = 'a3b4e1bf633b'

TABLE = 'provisioning'


def upgrade():
    op.drop_column(TABLE, 'username')
    op.drop_column(TABLE, 'password')
    op.drop_column(TABLE, 'secure')
    op.drop_column(TABLE, 'private')


def downgrade():
    op.add_column(TABLE, sa.Column('username', sa.String(32), nullable=False, server_default=''))
    op.add_column(TABLE, sa.Column('password', sa.String(32), nullable=False, server_default=''))
    op.add_column(TABLE, sa.Column('secure', sa.Integer(), nullable=False, server_default='0'))
    op.add_column(TABLE, sa.Column('private', sa.Integer(), nullable=False, server_default='0'))

    op.alter_column(TABLE, 'username', server_default=None)
    op.alter_column(TABLE, 'password', server_default=None)
