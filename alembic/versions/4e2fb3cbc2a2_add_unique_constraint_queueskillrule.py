"""add_unique_constraint_queueskillrule

Revision ID: 4e2fb3cbc2a2
Revises: 129646f8f81f

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = '4e2fb3cbc2a2'
down_revision = '129646f8f81f'


def upgrade():
    op.alter_column('queueskillrule', 'name', unique=True, nullable=False)


def downgrade():
    op.alter_column('queueskillrule', 'name', unique=False, nullable=True)
