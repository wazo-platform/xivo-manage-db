"""remove_nullable_constraint_queuefeatures

Revision ID: 570d858c41d6
Revises: 6a08e32fadba

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = '570d858c41d6'
down_revision = '6a08e32fadba'


def upgrade():
    op.alter_column('queuefeatures', 'number', nullable=True, server_default=None)


def downgrade():
    op.alter_column('queuefeatures', 'number', nullable=False, server_default='')
