"""add_delete_cascade_fk_switchboard_member

Revision ID: b4fb4eb3cf8e
Revises: 2f786b1077f9

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = 'b4fb4eb3cf8e'
down_revision = '2f786b1077f9'


def upgrade():
    op.execute(
        'DELETE FROM switchboard_member_user WHERE user_uuid NOT IN (SELECT DISTINCT uuid FROM userfeatures)'
    )
    op.execute(
        'DELETE FROM switchboard WHERE uuid NOT IN (SELECT DISTINCT switchboard_uuid FROM switchboard_member_user)'
    )
    op.drop_constraint(
        "switchboard_member_user_switchboard_uuid_fkey",
        "switchboard_member_user",
        type_="foreignkey",
    )
    op.drop_constraint(
        "switchboard_member_user_user_uuid_fkey",
        "switchboard_member_user",
        type_="foreignkey",
    )
    op.create_foreign_key(
        None,
        "switchboard_member_user",
        "switchboard",
        ["switchboard_uuid"],
        ["uuid"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        None,
        "switchboard_member_user",
        "userfeatures",
        ["user_uuid"],
        ["uuid"],
        ondelete="CASCADE",
    )


def downgrade():
    op.drop_constraint(
        "switchboard_member_user_switchboard_uuid_fkey",
        "switchboard_member_user",
        type_="foreignkey",
    )
    op.drop_constraint(
        "switchboard_member_user_user_uuid_fkey",
        "switchboard_member_user",
        type_="foreignkey",
    )
    op.create_foreign_key(
        None, "switchboard_member_user", "switchboard", ["switchboard_uuid"], ["uuid"]
    )
    op.create_foreign_key(
        None, "switchboard_member_user", "userfeatures", ["user_uuid"], ["uuid"]
    )
