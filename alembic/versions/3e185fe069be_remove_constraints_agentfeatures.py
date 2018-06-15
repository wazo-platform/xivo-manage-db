"""remove_constraints_agentfeatures

Revision ID: 3e185fe069be
Revises: 570d858c41d6

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = '3e185fe069be'
down_revision = '570d858c41d6'


def upgrade():
    op.alter_column('agentfeatures', 'firstname', nullable=True, server_default=None)
    op.alter_column('agentfeatures', 'lastname', nullable=True, server_default=None)
    op.alter_column('agentfeatures', 'passwd', nullable=True)
    op.alter_column('agentfeatures', 'language', nullable=True)
    op.alter_column('agentfeatures', 'context', nullable=True)
    op.alter_column('agentfeatures', 'description', nullable=True)


def downgrade():
    op.alter_column('agentfeatures', 'firstname', nullable=False, server_default='')
    op.alter_column('agentfeatures', 'lastname', nullable=False, server_default='')
    op.alter_column('agentfeatures', 'passwd', nullable=False)
    op.alter_column('agentfeatures', 'language', nullable=False)
    op.alter_column('agentfeatures', 'context', nullable=False)
    op.alter_column('agentfeatures', 'description', nullable=False)
