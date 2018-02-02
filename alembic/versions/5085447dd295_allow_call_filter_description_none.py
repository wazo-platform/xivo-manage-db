"""allow-call-filter-description-none

Revision ID: 5085447dd295
Revises: 2991705be1ec

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = '5085447dd295'
down_revision = '2991705be1ec'


def upgrade():
    op.alter_column('callfilter', 'description', nullable=True)


def downgrade():
    op.alter_column('callfilter', 'description', nullable=False)
