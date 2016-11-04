"""remove_nullable_constraint_groupfeatures

Revision ID: 58d561775bf3
Revises: 18b419c519f4

"""

# revision identifiers, used by Alembic.
revision = '58d561775bf3'
down_revision = '18b419c519f4'

from alembic import op


def upgrade():
    op.alter_column('groupfeatures', 'number', nullable=True, server_default=None)
    op.alter_column('groupfeatures', 'context', nullable=True)


def downgrade():
    op.alter_column('groupfeatures', 'number', nullable=False, server_default='')
    op.alter_column('groupfeatures', 'context', nullable=False)
