"""remove_nullable_constraint_queueskillrule

Revision ID: 315f74edddb1
Revises: 1f272484c083

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = '315f74edddb1'
down_revision = '1f272484c083'


def upgrade():
    op.alter_column('queueskillrule', 'name', nullable=True, server_default=None)


def downgrade():
    op.alter_column('queueskillrule', 'name', nullable=False, server_default='')
