"""queue timeout may be null

Revision ID: 4cf59c82b51e
Revises: 234745874c55

"""

# revision identifiers, used by Alembic.
revision = '4cf59c82b51e'
down_revision = '234745874c55'

from alembic import op


def upgrade():
    op.alter_column('queuefeatures', 'timeout', server_default=None, nullable=True)


def downgrade():
    op.alter_column('queuefeatures', 'timeout', server_default='0', nullable=False)
