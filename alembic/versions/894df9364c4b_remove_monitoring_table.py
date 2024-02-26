"""remove-monitoring-table

Revision ID: 894df9364c4b
Revises: e521f996dfaf

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '894df9364c4b'
down_revision = 'e521f996dfaf'


def upgrade():
    op.drop_table('monitoring')


def downgrade():
    op.create_table(
        'monitoring',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('maintenance', sa.Integer, nullable=False, server_default='0'),
        sa.Column('alert_emails', sa.String(4096)),
        sa.Column('max_call_duration', sa.Integer),
    )
