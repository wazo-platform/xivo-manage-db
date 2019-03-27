"""alter provisioning remove not null constraint

Revision ID: 700711f75ee6
Revises: 4c79fd76bccb

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '700711f75ee6'
down_revision = '4c79fd76bccb'

TABLE = 'provisioning'


def upgrade():
    op.alter_column(TABLE, 'net4_ip', nullable=True)
    op.alter_column(TABLE, 'net4_ip_rest', nullable=True)


def downgrade():
    op.alter_column(TABLE, 'net4_ip', nullable=False)
    op.alter_column(TABLE, 'net4_ip_rest', nullable=False)
