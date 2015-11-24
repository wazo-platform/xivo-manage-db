"""add xivo directory fields

Revision ID: 2f7e5c4119bc
Revises: 537774d3845a

"""

# revision identifiers, used by Alembic.
revision = '2f7e5c4119bc'
down_revision = '537774d3845a'

from alembic import op
from sqlalchemy.schema import Column
from sqlalchemy.types import Boolean, Text


def upgrade():
    op.add_column('directories',
            Column('xivo_username', Text))
    op.add_column('directories',
            Column('xivo_password', Text))
    op.add_column('directories',
            Column('xivo_verify_certificate', Boolean, nullable=False, server_default='False'))
    op.add_column('directories',
            Column('xivo_custom_ca_path', Text))


def downgrade():
    op.drop_column('directories', 'xivo_username')
    op.drop_column('directories', 'xivo_password')
    op.drop_column('directories', 'xivo_verify_certificate')
    op.drop_column('directories', 'xivo_custom_ca_path')
