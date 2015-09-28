"""rename enableautomon to enableonlinerec

Revision ID: 2ea8d6cb26f6
Revises: 86511ef5d49

"""

# revision identifiers, used by Alembic.
revision = '2ea8d6cb26f6'
down_revision = '86511ef5d49'

from alembic import op


def upgrade():
    op.alter_column('userfeatures', 'enableautomon', new_column_name='enableonlinerec')


def downgrade():
    op.alter_column('userfeatures', 'enableonlinerec', new_column_name='enableautomon')
