"""disallow_null_type_for_app_dest_node

Revision ID: 0c84ec128899
Revises: 11cfb4ff787d

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = '0c84ec128899'
down_revision = '11cfb4ff787d'


def upgrade():
    op.alter_column('application_dest_node', 'type', nullable=False)


def downgrade():
    op.alter_column('application_dest_node', 'type', nullable=True)
