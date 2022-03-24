"""meeting: require authorization not null

Revision ID: 2b65d248c2ad
Revises: c9ed2541b284

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = '2b65d248c2ad'
down_revision = 'c9ed2541b284'


def upgrade():
    op.alter_column('meeting', 'require_authorization', nullable=False)


def downgrade():
    op.alter_column('meeting', 'require_authorization', nullable=True)
