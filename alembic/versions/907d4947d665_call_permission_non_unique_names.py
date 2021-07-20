"""call_permission non unique names

Revision ID: 907d4947d665
Revises: cb5666745311

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = '907d4947d665'
down_revision = 'cb5666745311'

TBL_NAME = 'rightcall'
OLD_CONSTRAINT_NAME = 'rightcall_name_key'
NEW_CONSTRAINT_NAME = 'rightcall_name_tenant_uuid_key'


def upgrade():
    op.create_unique_constraint(NEW_CONSTRAINT_NAME, TBL_NAME, ['name', 'tenant_uuid'])
    op.drop_constraint(OLD_CONSTRAINT_NAME, TBL_NAME)


def downgrade():
    op.create_unique_constraint(OLD_CONSTRAINT_NAME, TBL_NAME, ['name'])
    op.drop_constraint(NEW_CONSTRAINT_NAME, TBL_NAME)
