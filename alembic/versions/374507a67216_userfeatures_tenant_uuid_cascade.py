"""userfeatures_tenant_uuid_cascade

Revision ID: 374507a67216
Revises: 476a2700b4c2

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = '374507a67216'
down_revision = '476a2700b4c2'

constraint_name = 'userfeatures_tenant_uuid_fkey'


def upgrade():
    op.drop_constraint(constraint_name, 'userfeatures')
    op.create_foreign_key(
        constraint_name,
        'userfeatures', 'tenant',
        ['tenant_uuid'], ['uuid'],
        ondelete='CASCADE',
    )


def downgrade():
    op.drop_constraint(constraint_name, 'userfeatures')
    op.create_foreign_key(
        constraint_name,
        'userfeatures', 'tenant',
        ['tenant_uuid'], ['uuid'],
    )
