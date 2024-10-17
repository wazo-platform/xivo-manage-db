"""add trunk outgoing-caller-id-format

Revision ID: d80c07b01d39
Revises: 2dbf602f5e31

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd80c07b01d39'
down_revision = '2dbf602f5e31'

TABLE_NAME = 'trunkfeatures'
COLUMN_NAME = 'outgoing_caller_id_format'


def upgrade():
    op.add_column(
        TABLE_NAME,
        sa.Column(
            COLUMN_NAME,
            sa.Text,
            sa.CheckConstraint("outgoing_caller_id_format in ('+E164', 'E164', 'national')"),
            server_default='+E164',
            nullable=False,
        )
    )


def downgrade():
    op.drop_column(TABLE_NAME, COLUMN_NAME)
