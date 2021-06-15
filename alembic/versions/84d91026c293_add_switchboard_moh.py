"""add switchboard moh

Revision ID: 84d91026c293
Revises: 9eeb96b396a7

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84d91026c293'
down_revision = '9eeb96b396a7'

COLUMN_NAMES = [
    'hold_moh_uuid',
    'queue_moh_uuid',
]


def upgrade():
    for column_name in COLUMN_NAMES:
        op.add_column(
            'switchboard',
            sa.Column(
                column_name,
                sa.String(38),
                sa.ForeignKey('moh.uuid', ondelete='SET NULL'),
                nullable=True,
            )
        )


def downgrade():
    for column_name in COLUMN_NAMES:
        op.drop_column('switchboard', column_name)
