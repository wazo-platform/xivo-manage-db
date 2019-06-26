"""add_answer_to_application_dest_node

Revision ID: d0411d361d57
Revises: 4fe20686380b

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0411d361d57'
down_revision = '4fe20686380b'


def upgrade():
    op.add_column(
        'application_dest_node',
        sa.Column('answer', sa.Boolean, nullable=False, server_default='True')
    )
    op.alter_column('application_dest_node', 'answer', server_default=None)


def downgrade():
    op.drop_column('application_dest_node', 'answer')
