"""add_unique_constraint_to_user_email

Revision ID: 4fe888586ba3
Revises: 3420040c5650

"""

# revision identifiers, used by Alembic.
revision = '4fe888586ba3'
down_revision = '3420040c5650'

from alembic import op


def upgrade():
    op.create_unique_constraint('userfeatures_email', 'userfeatures', ['email'])


def downgrade():
    op.drop_constraint('userfeatures_email', 'userfeatures')
