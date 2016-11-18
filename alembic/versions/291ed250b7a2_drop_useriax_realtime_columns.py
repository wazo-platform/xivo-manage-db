"""drop useriax realtime columns

Revision ID: 291ed250b7a2
Revises: 6e196b7526a

"""

# revision identifiers, used by Alembic.
revision = '291ed250b7a2'
down_revision = '6e196b7526a'

from alembic import op
from sqlalchemy import Column, Integer, String


def upgrade():
    op.drop_column('useriax', 'ipaddr')
    op.drop_column('useriax', 'regseconds')


def downgrade():
    op.add_column('useriax', Column('ipaddr', String(255), nullable=False, server_default=''))
    op.add_column('useriax', Column('regseconds', Integer, nullable=False, server_default='0'))
