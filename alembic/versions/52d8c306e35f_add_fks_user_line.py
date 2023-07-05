"""add_fks_user_line

Revision ID: 52d8c306e35f
Revises: 15389f63cfdd

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = '52d8c306e35f'
down_revision = '15389f63cfdd'


def upgrade():
    op.execute('DELETE FROM user_line WHERE user_id NOT IN (SELECT DISTINCT id FROM userfeatures)')
    op.execute('DELETE FROM linefeatures WHERE id NOT IN (SELECT DISTINCT line_id FROM user_line)')
    op.drop_constraint("user_line_user_id_fkey", "user_line", type_="foreignkey")
    op.drop_constraint("user_line_line_id_fkey", "user_line", type_="foreignkey")
    op.create_foreign_key(
        None,
        "user_line",
        "userfeatures",
        ["user_id"],
        ["id"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        None,
        "user_line",
        "linefeatures",
        ["line_id"],
        ["id"],
        ondelete="CASCADE",
    )


def downgrade():
    op.drop_constraint("user_line_user_id_fkey", "user_line", type_="foreignkey")
    op.drop_constraint("user_line_line_id_fkey", "user_line", type_="foreignkey")
    op.create_foreign_key(
        None,
        "user_line",
        "userfeatures",
        ["user_id"],
        ["id"],
    )
    op.create_foreign_key(
        None,
        "user_line",
        "linefeatures",
        ["line_id"],
        ["id"],
    )
