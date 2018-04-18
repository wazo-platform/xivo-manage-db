"""add-subscription-to-userfeatures

Revision ID: 4a5a1c3eb52f
Revises: 68507181de97

"""

import datetime

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a5a1c3eb52f'
down_revision = '68507181de97'


def upgrade():
    op.add_column(
        'userfeatures',
        sa.Column(
            'created_at',
            sa.DateTime,
            default=datetime.datetime.utcnow,
            server_default=sa.text("(now() at time zone 'utc')")
        )
    )
    op.add_column('userfeatures', sa.Column('subscription_type', sa.Integer, nullable=False, server_default='0'))


def downgrade():
    op.drop_column('userfeatures', 'subscription_type')
    op.drop_column('userfeatures', 'created_at')
