"""add ondelete cascade funckey dest

Revision ID: 4e6562f15b59
Revises: 7e13ede8dbb1

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = '4e6562f15b59'
down_revision = '7e13ede8dbb1'


def upgrade():
    op.drop_constraint("func_key_dest_user_user_id_fkey", "func_key_dest_user", type_="foreignkey")
    op.create_foreign_key(
        None,
        "func_key_dest_user",
        "userfeatures",
        ["user_id"],
        ["id"],
        ondelete="CASCADE",
    )

    op.drop_constraint("func_key_dest_queue_queue_id_fkey", "func_key_dest_queue", type_="foreignkey")
    op.create_foreign_key(
        None,
        "func_key_dest_queue",
        "queuefeatures",
        ["queue_id"],
        ["id"],
        ondelete="CASCADE",
    )

    op.drop_constraint("func_key_dest_parking_parking_lot_id_fkey", "func_key_dest_parking", type_="foreignkey")
    op.create_foreign_key(
        None,
        "func_key_dest_parking",
        "parking_lot",
        ["parking_lot_id"],
        ["id"],
        ondelete="CASCADE",
    )

    op.drop_constraint("func_key_dest_service_feature_extension_uuid_fkey", "func_key_dest_service", type_="foreignkey")
    op.create_foreign_key(
        None,
        "func_key_dest_service",
        "feature_extension",
        ["feature_extension_uuid"],
        ["uuid"],
        ondelete="CASCADE",
    )


    op.drop_constraint("func_key_dest_groupmember_group_id_fkey", "func_key_dest_groupmember", type_="foreignkey")
    op.create_foreign_key(
        None,
        "func_key_dest_groupmember",
        "groupfeatures",
        ["group_id"],
        ["id"],
        ondelete="CASCADE",
    )

    op.drop_constraint("func_key_dest_groupmember_feature_extension_uuid_fkey", "func_key_dest_groupmember", type_="foreignkey")
    op.create_foreign_key(
        None,
        "func_key_dest_groupmember",
        "feature_extension",
        ["feature_extension_uuid"],
        ["uuid"],
        ondelete="CASCADE",
    )

    op.drop_constraint("func_key_dest_group_group_id_fkey", "func_key_dest_group", type_="foreignkey")
    op.create_foreign_key(
        None,
        "func_key_dest_group",
        "groupfeatures",
        ["group_id"],
        ["id"],
        ondelete="CASCADE",
    )

    op.drop_constraint("func_key_dest_paging_paging_id_fkey", "func_key_dest_paging", type_="foreignkey")
    op.create_foreign_key(
        None,
        "func_key_dest_paging",
        "paging",
        ["paging_id"],
        ["id"],
        ondelete="CASCADE",
    )

    op.drop_constraint("func_key_dest_park_position_parking_lot_id_fkey", "func_key_dest_park_position", type_="foreignkey")
    op.create_foreign_key(
        None,
        "func_key_dest_park_position",
        "parking_lot",
        ["parking_lot_id"],
        ["id"],
        ondelete="CASCADE",
    )


def downgrade():
    op.drop_constraint("func_key_dest_user_user_id_fkey", "func_key_dest_user", type_="foreignkey")
    op.create_foreign_key(
        None,
        "func_key_dest_user",
        "userfeatures",
        ["user_id"],
        ["id"]
    )

    op.drop_constraint("func_key_dest_queue_queue_id_fkey", "func_key_dest_queue", type_="foreignkey")
    op.create_foreign_key(
        None,
        "func_key_dest_queue",
        "queuefeatures",
        ["queue_id"],
        ["id"]
    )

    op.drop_constraint("func_key_dest_parking_parking_lot_id_fkey", "func_key_dest_parking", type_="foreignkey")
    op.create_foreign_key(
        None,
        "func_key_dest_parking",
        "parking_lot",
        ["parking_lot_id"],
        ["id"]
    )

    op.drop_constraint("func_key_dest_service_feature_extension_uuid_fkey", "func_key_dest_service", type_="foreignkey")
    op.create_foreign_key(
        None,
        "func_key_dest_service",
        "feature_extension",
        ["feature_extension_uuid"],
        ["uuid"],
    )

    op.drop_constraint("func_key_dest_groupmember_group_id_fkey", "func_key_dest_groupmember", type_="foreignkey")
    op.create_foreign_key(
        None,
        "func_key_dest_groupmember",
        "groupfeatures",
        ["group_id"],
        ["id"],
    )

    op.drop_constraint("func_key_dest_groupmember_feature_extension_uuid_fkey", "func_key_dest_groupmember", type_="foreignkey")
    op.create_foreign_key(
        None,
        "func_key_dest_groupmember",
        "feature_extension",
        ["feature_extension_uuid"],
        ["uuid"],
    )

    op.drop_constraint("func_key_dest_group_group_id_fkey", "func_key_dest_group", type_="foreignkey")
    op.create_foreign_key(
        None,
        "func_key_dest_group",
        "groupfeatures",
        ["group_id"],
        ["id"],
    )

    op.drop_constraint("func_key_dest_paging_paging_id_fkey", "func_key_dest_paging", type_="foreignkey")
    op.create_foreign_key(
        None,
        "func_key_dest_paging",
        "paging",
        ["paging_id"],
        ["id"],
    )

    op.drop_constraint("func_key_dest_park_position_parking_lot_id_fkey", "func_key_dest_park_position", type_="foreignkey")
    op.create_foreign_key(
        None,
        "func_key_dest_park_position",
        "parking_lot",
        ["parking_lot_id"],
        ["id"],
    )
