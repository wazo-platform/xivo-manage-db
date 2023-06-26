"""add_fk_context_for_contextmember

Revision ID: 85a827ab4711
Revises: 9869009eb5b3

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = '85a827ab4711'
down_revision = '9869009eb5b3'



def upgrade():
    op.create_foreign_key(
        None,
        "contextmember",
        "context",
        ["context"],
        ["name"],
        ondelete="CASCADE",
    )


def downgrade():
    op.drop_constraint(
        "contextmember_context_fkey",
        "context",
        type_="foreignkey")
