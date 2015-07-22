"""activate blf by default

Revision ID: 44c6b8d8c196
Revises: 4a80d0e24028

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = '44c6b8d8c196'
down_revision = '4a80d0e24028'


def upgrade():
    op.alter_column('func_key_mapping', 'blf', server_default='True')


def downgrade():
    op.alter_column('func_key_mapping', 'blf', server_default='False')
