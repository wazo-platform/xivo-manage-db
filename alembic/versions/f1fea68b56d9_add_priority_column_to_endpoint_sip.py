"""add-priority-column-to-endpoint-sip

Revision ID: f1fea68b56d9
Revises: ee773d263d87

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1fea68b56d9'
down_revision = 'ee773d263d87'


def upgrade():
    op.add_column('endpoint_sip_template', sa.Column('priority', sa.Integer))


def downgrade():
    op.drop_column('endpoint_sip_template', 'priority')
