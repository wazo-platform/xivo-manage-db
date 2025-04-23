"""add ondelete cascade funckey dest

Revision ID: 4e6562f15b59
Revises: 7e13ede8dbb1

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = '4e6562f15b59'
down_revision = '7e13ede8dbb1'

relationships = [
    ("func_key_dest_user", "user_id", "userfeatures", "id"),
    ("func_key_dest_queue", "queue_id", "queuefeatures", "id"),
    ("func_key_dest_parking", "parking_lot_id", "parking_lot", "id"),
    ("func_key_dest_service", "feature_extension_uuid", "feature_extension", "uuid"),
    ("func_key_dest_groupmember", "group_id", "groupfeatures", "id"),
    ("func_key_dest_groupmember", "feature_extension_uuid", "feature_extension", "uuid"),
    ("func_key_dest_group", "group_id", "groupfeatures", "id"),
    ("func_key_dest_paging", "paging_id", "paging", "id"),
    ("func_key_dest_park_position", "parking_lot_id", "parking_lot", "id"),
    ("func_key_dest_features", "features_id", "features", "id"),
    ("func_key_dest_forward", "feature_extension_uuid", "feature_extension", "uuid"),
    ("func_key_dest_agent", "agent_id", "agentfeatures", "id"),
    ("func_key_dest_agent", "feature_extension_uuid", "feature_extension", "uuid"),
]


def create_cascade_foreign_key_delete_orphans(
        source_table_name, source_column_name, target_table_name, target_column_name
    ):
    op.drop_constraint(
        f"{source_table_name}_{source_column_name}_fkey", source_table_name, type_="foreignkey"
    )
    op.execute(
        f'DELETE FROM {source_table_name} WHERE {source_column_name} NOT IN '
        f'(SELECT DISTINCT {target_column_name} FROM {target_table_name});'
    )
    op.create_foreign_key(
        None,
        source_table_name,
        target_table_name,
        [source_column_name],
        [target_column_name],
        ondelete="CASCADE",
    )


def delete_cascade_foreign_key(
        source_table_name, source_column_name, target_table_name, target_column_name
    ):
    op.drop_constraint(
        f"{source_table_name}_{source_column_name}_fkey", source_table_name, type_="foreignkey"
    )
    op.create_foreign_key(
        None,
        source_table_name,
        target_table_name,
        [source_column_name],
        [target_column_name],
    )


def upgrade():
    for source_table, source_column, target_table, target_column in relationships:
        create_cascade_foreign_key_delete_orphans(
            source_table, source_column, target_table, target_column
        )


def downgrade():
    for source_table, source_column, target_table, target_column in relationships:
        delete_cascade_foreign_key(source_table, source_column, target_table, target_column)
