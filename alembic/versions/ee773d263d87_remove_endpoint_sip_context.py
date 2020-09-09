"""remove-endpoint-sip-context

Revision ID: ee773d263d87
Revises: 42b0914ed3e6

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee773d263d87'
down_revision = 'ea74eca400ce'


def upgrade():
    op.drop_column('endpoint_sip', 'context_id')


def downgrade():
    op.add_column(
        'endpoint_sip',
        sa.Column('context_id', sa.Integer, sa.ForeignKey('context.id')),
    )
