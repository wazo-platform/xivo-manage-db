"""add group uuid

Revision ID: 382aaefc59ec
Revises: 9442da3b20b6

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = '382aaefc59ec'
down_revision = '9442da3b20b6'


def upgrade():
    op.add_column(
        'groupfeatures',
        sa.Column(
            'uuid',
            UUID,
            server_default=sa.text('uuid_generate_v4()'),
            nullable=False,
        )
    )
    op.create_index(
        index_name='groupfeatures__idx__uuid',
        table_name='groupfeatures',
        columns=['uuid'],
    )


def downgrade():
    op.drop_column('groupfeatures', 'uuid')
