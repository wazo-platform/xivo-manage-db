"""add_unique_constraint_queueskillrule

Revision ID: 4e2fb3cbc2a2
Revises: 129646f8f81f

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = '4e2fb3cbc2a2'
down_revision = '129646f8f81f'

table_name = 'queueskillrule'
constraint_name = f'{table_name}_name_key'


def upgrade():
    op.alter_column(table_name, 'name', nullable=False)
    op.create_unique_constraint(constraint_name, table_name, ['name'])


def downgrade():
    op.drop_constraint(constraint_name, table_name)
    op.alter_column(table_name, 'name', nullable=True)
