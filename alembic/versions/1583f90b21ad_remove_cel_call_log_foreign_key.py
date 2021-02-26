"""remove-cel-call-log-foreign-key

Revision ID: 1583f90b21ad
Revises: 867bd9268824

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = '1583f90b21ad'
down_revision = '867bd9268824'

constraint_name = 'cel_call_log_id_fkey'


def upgrade():
    op.drop_constraint(constraint_name, 'cel')


def downgrade():
    op.create_foreign_key(
        constraint_name,
        'cel',
        'call_log',
        ['call_log_id'],
        ['id'],
        ondelete='SET NULL',
    )
