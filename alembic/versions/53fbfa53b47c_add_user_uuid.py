"""add user UUID

Revision ID: 53fbfa53b47c
Revises: e66504d94e2e

"""

# revision identifiers, used by Alembic.
revision = '53fbfa53b47c'
down_revision = 'e66504d94e2e'

from alembic import op
import sqlalchemy as sa

table_name = 'user'
column_name = 'uuid'
constraint_name = '{}_{}_key'.format(table_name, column_name)


def upgrade():
    op.add_column(
        table_name,
        sa.Column(
            column_name,
            sa.String(38),
            nullable=False,
            server_default=sa.text('uuid_generate_v4()')))
    op.create_unique_constraint(constraint_name, table_name, [column_name])


def downgrade():
    op.drop_constraint(constraint_name, table_name)
    op.drop_column(table_name, column_name)
