"""add check constraint on phonenumber table for main==>shared

Revision ID: a93b2625be0d
Revises: 59c0eedf8853

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a93b2625be0d'
down_revision = 'd82b12082862'

phone_number_table = sa.table(
    'phone_number',
)


def upgrade():
    op.create_check_constraint(
        'phone_number_shared_if_main',
        'phone_number',
        'CASE WHEN main THEN shared ELSE true END'
    )


def downgrade():
    op.drop_constraint('phone_number_shared_if_main', 'phone_number')
