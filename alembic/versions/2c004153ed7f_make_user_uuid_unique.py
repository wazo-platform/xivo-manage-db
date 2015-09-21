"""make user.uuid unique

Revision ID: 2c004153ed7f
Revises: 1c3eb7380750

"""

# revision identifiers, used by Alembic.
revision = '2c004153ed7f'
down_revision = '1c3eb7380750'

from alembic import op


def upgrade():
    op.create_unique_constraint('userfeatures_uuid', 'userfeatures', ['uuid'])


def downgrade():
    op.drop_constraint('userfeatures_uuid', 'userfeatures')
