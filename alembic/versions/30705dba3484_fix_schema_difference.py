"""fix-schema-difference

Revision ID: 30705dba3484
Revises: 1d5d4e41d708

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30705dba3484'
down_revision = '1d5d4e41d708'


def upgrade():
    op.alter_column('func_key_dest_agent', 'feature_extension_uuid', nullable=False)
    op.alter_column('func_key_dest_forward', 'feature_extension_uuid', nullable=False)
    op.alter_column('func_key_dest_groupmember', 'feature_extension_uuid', nullable=False)
    op.alter_column('func_key_dest_service', 'feature_extension_uuid', nullable=False)


def downgrade():
    op.alter_column('func_key_dest_agent', 'feature_extension_uuid', nullable=True)
    op.alter_column('func_key_dest_forward', 'feature_extension_uuid', nullable=True)
    op.alter_column('func_key_dest_groupmember', 'feature_extension_uuid', nullable=True)
    op.alter_column('func_key_dest_service', 'feature_extension_uuid', nullable=True)
