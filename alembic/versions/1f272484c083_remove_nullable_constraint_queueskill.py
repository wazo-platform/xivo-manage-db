"""remove_nullable_constraint_queueskill

Revision ID: 1f272484c083
Revises: 8452bc3d5d67

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = '1f272484c083'
down_revision = '8452bc3d5d67'


def upgrade():
    op.alter_column('queueskill', 'catid', nullable=True, server_default=None)


def downgrade():
    op.alter_column('queueskill', 'catid', nullable=False, server_default='1')
