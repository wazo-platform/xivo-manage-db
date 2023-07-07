"""add_fk_line_context

Revision ID: 2f786b1077f9
Revises: 52d8c306e35f

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = '2f786b1077f9'
down_revision = '52d8c306e35f'


def upgrade():
    op.create_foreign_key(
        None,
        "linefeatures",
        "context",
        ["context"],
        ["name"],
        ondelete="CASCADE",
    )


def downgrade():
    op.drop_constraint("linefeatures_context_fkey", "linefeatures", type_="foreignkey")
