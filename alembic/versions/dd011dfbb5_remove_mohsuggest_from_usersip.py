"""remove mohsuggest from UserSIP

Revision ID: dd011dfbb5
Revises: 5073b1fa473e
XiVO Version: 14.11

"""

# revision identifiers, used by Alembic.
revision = 'dd011dfbb5'
down_revision = '5073b1fa473e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.drop_column('usersip', 'mohsuggest')


def downgrade():
    op.add_column('usersip', sa.Column('mohsuggest', sa.String(80)))
