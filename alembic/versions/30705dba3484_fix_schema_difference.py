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

    op.create_unique_constraint(
        'feature_extension_exten_key',
        'feature_extension',
        ['exten'],
    )

    op.create_unique_constraint(
        'func_key_dest_agent_agent_id_feature_extension_uuid_key',
        'func_key_dest_agent',
        ['agent_id', 'feature_extension_uuid'],
    )
    op.create_unique_constraint(
        'func_key_dest_groupmember_group_id_feature_extension_uuid_key',
        'func_key_dest_groupmember',
        ['group_id', 'feature_extension_uuid'],
    )
    op.create_primary_key(
        'func_key_dest_forward_pkey',
        'func_key_dest_forward',
        ['func_key_id', 'destination_type_id', 'feature_extension_uuid'],
    )
    op.create_primary_key(
        'func_key_dest_service_pkey',
        'func_key_dest_service',
        ['func_key_id', 'destination_type_id', 'feature_extension_uuid'],
    )


def downgrade():
    op.drop_constraint(
        'func_key_dest_service_pkey',
        'func_key_dest_service',
    )
    op.drop_constraint(
        'func_key_dest_groupmember_group_id_feature_extension_uuid_key',
        'func_key_dest_groupmember',
    )
    op.drop_constraint(
        'func_key_dest_forward_pkey',
        'func_key_dest_forward',
    )
    op.drop_constraint(
        'func_key_dest_agent_agent_id_feature_extension_uuid_key',
        'func_key_dest_agent',
    )

    op.drop_constraint('feature_extension_exten_key', 'feature_extension')

    op.alter_column('func_key_dest_agent', 'feature_extension_uuid', nullable=True)
    op.alter_column('func_key_dest_forward', 'feature_extension_uuid', nullable=True)
    op.alter_column('func_key_dest_groupmember', 'feature_extension_uuid', nullable=True)
    op.alter_column('func_key_dest_service', 'feature_extension_uuid', nullable=True)
