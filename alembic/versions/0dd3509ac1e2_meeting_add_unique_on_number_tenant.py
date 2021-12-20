"""meeting-add-unique-on-number-tenant

Revision ID: 0dd3509ac1e2
Revises: b7d3c4701095

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = '0dd3509ac1e2'
down_revision = 'b7d3c4701095'


def upgrade():
    op.create_unique_constraint(
        'meeting_number_tenant_uuid_key',
        'meeting',
        ['number', 'tenant_uuid'],
    )


def downgrade():
    op.drop_constraint('meeting_number_tenant_uuid_key', 'meeting')
