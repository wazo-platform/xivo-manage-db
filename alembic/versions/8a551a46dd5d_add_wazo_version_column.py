"""add_wazo_version_column

Revision ID: 8a551a46dd5d
Revises: 198c5bc02abf

"""

# revision identifiers, used by Alembic.
revision = '8a551a46dd5d'
down_revision = '198c5bc02abf'

from alembic import op
from sqlalchemy.schema import Column
from sqlalchemy.types import String


def upgrade():
    op.add_column('infos', Column('wazo_version', String(64), nullable=False, server_default='17.01'))
    op.alter_column('infos', 'wazo_version', server_default=None)


def downgrade():
    op.drop_column('infos', 'wazo_version')
