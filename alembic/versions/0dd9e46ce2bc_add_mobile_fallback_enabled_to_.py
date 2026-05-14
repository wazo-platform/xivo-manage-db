"""add_mobile_fallback_enabled_to_userfeatures

Revision ID: 0dd9e46ce2bc
Revises: 8863a45bcbd0

"""

import sqlalchemy as sa

from alembic import op
from sqlalchemy.sql import text


# revision identifiers, used by Alembic.
revision = '0dd9e46ce2bc'
down_revision = '8863a45bcbd0'


def upgrade():
    op.add_column(
        'userfeatures',
        sa.Column(
            'mobile_fallback_enabled',
            sa.Boolean,
            nullable=False,
            server_default=text('false'),
        ),
    )


def downgrade():
    op.drop_column('userfeatures', 'mobile_fallback_enabled')
