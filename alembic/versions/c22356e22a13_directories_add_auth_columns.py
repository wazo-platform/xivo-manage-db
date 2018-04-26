"""directories: add auth columns

Revision ID: c22356e22a13
Revises: 4cf687f2c0eb

"""

# revision identifiers, used by Alembic.
revision = 'c22356e22a13'
down_revision = '4cf687f2c0eb'


from alembic import op
import sqlalchemy as sa

table = 'directories'


def upgrade():
    op.add_column(table, sa.Column('auth_backend', sa.Text))
    op.add_column(table, sa.Column('auth_host', sa.Text))
    op.add_column(table, sa.Column('auth_port', sa.Integer))
    op.add_column(
        table,
        sa.Column('auth_verify_certificate', sa.Boolean, nullable=False, server_default='False'),
    )
    op.add_column(table, sa.Column('auth_custom_ca_path', sa.Text))


def downgrade():
    for column in ('auth_backend', 'auth_host', 'auth_port', 'auth_verify_certificate', 'auth_custom_ca_path'):
        op.drop_column(table, column)
