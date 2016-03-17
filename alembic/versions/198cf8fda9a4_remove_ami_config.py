"""remove ami config

Revision ID: 198cf8fda9a4
Revises: 3c72c43e39fa

"""

# revision identifiers, used by Alembic.
revision = '198cf8fda9a4'
down_revision = '3c72c43e39fa'

from alembic import op
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer


def upgrade():
    op.drop_column('ctimain', 'ami_ip')
    op.drop_column('ctimain', 'ami_port')
    op.drop_column('ctimain', 'ami_login')
    op.drop_column('ctimain', 'ami_password')


def downgrade():
    op.add_column('ctimain', Column('ami_ip', String(16)))
    op.add_column('ctimain', Column('ami_port', Integer))
    op.add_column('ctimain', Column('ami_login', String(64)))
    op.add_column('ctimain', Column('ami_password', String(64)))
