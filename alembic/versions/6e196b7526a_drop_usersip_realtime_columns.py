"""drop usersip realtime columns

Revision ID: 6e196b7526a
Revises: 3284584a535c

"""

# revision identifiers, used by Alembic.
revision = '6e196b7526a'
down_revision = '3284584a535c'

from alembic import op
from sqlalchemy import Column, Integer, String


def upgrade():
    op.drop_column('usersip', 'fullcontact')
    op.drop_column('usersip', 'ipaddr')
    op.drop_column('usersip', 'regseconds')
    op.drop_column('usersip', 'regserver')
    op.drop_column('usersip', 'lastms')


def downgrade():
    op.add_column('usersip', Column('fullcontact', String(255)))
    op.add_column('usersip', Column('ipaddr', String(255), nullable=False, server_default=''))
    op.add_column('usersip', Column('regseconds', Integer, nullable=False, server_default='0'))
    op.add_column('usersip', Column('regserver', String(20)))
    op.add_column('usersip', Column('lastms', String(15), nullable=False, server_default=''))
