"""add_fk_func_key_mapping

Revision ID: 91d6933efd3e
Revises: 8fe383847bcc

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = '91d6933efd3e'
down_revision = '2509c5ef5044'


def upgrade():
    op.drop_constraint("func_key_mapping_template_id_fkey", "func_key_mapping", type_="foreignkey")
    op.create_foreign_key(
        None,
        "func_key_mapping",
        "func_key_template",
        ["template_id"],
        ["id"],
        ondelete="CASCADE",
    )


def downgrade():
    op.drop_constraint("func_key_mapping_template_id_fkey", "func_key_mapping", type_="foreignkey")
    op.create_foreign_key(
        None,
        "func_key_mapping",
        "func_key_template",
        ["template_id"],
        ["id"],
    )
