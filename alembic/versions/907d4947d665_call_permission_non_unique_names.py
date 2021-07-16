"""call_permission non unique names

Revision ID: 907d4947d665
Revises: cb5666745311

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = '907d4947d665'
down_revision = 'cb5666745311'

TBL_NAME = 'rightcall'
CONSTRAINT_NAME = 'rightcall_name_key'


def upgrade():
    op.drop_constraint(CONSTRAINT_NAME, TBL_NAME)


def downgrade():
    op.create_unique_constraint(CONSTRAINT_NAME, TBL_NAME, ['name'])
