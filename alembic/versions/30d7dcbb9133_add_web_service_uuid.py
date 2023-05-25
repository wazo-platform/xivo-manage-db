"""add web service UUID

Revision ID: 30d7dcbb9133
Revises: 53fbfa53b47c

"""

# revision identifiers, used by Alembic.
revision = '30d7dcbb9133'
down_revision = '53fbfa53b47c'

from alembic import op
import sqlalchemy as sa


table_name = 'accesswebservice'
column_name = 'uuid'
constraint_name = f'{table_name}_{column_name}_key'


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
