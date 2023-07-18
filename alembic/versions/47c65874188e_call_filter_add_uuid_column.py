"""call filter add uuid column

Revision ID: 47c65874188e
Revises: 8353aca45dcb

"""

from alembic import op
import sqlalchemy as sa

from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = '47c65874188e'
down_revision = '8353aca45dcb'


def upgrade():
    op.add_column(
        'callfilter',
        sa.Column('uuid', UUID, server_default=sa.text('uuid_generate_v4()'), unique=True),
    )


def downgrade():
    op.drop_column('callfilter', 'uuid')
