"""add_fk_context_for_contextinclude

Revision ID: c86be8bc0377
Revises: 70171a0cbf15

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = 'c86be8bc0377'
down_revision = '70171a0cbf15'



def upgrade():
    op.create_foreign_key(
        None,
        "contextinclude",
        "context",
        ["context"],
        ["name"],
        ondelete="CASCADE",
        onupdate="CASCADE",
    )
    op.create_foreign_key(
        None,
        "contextinclude",
        "context",
        ["include"],
        ["name"],
        ondelete="CASCADE",
        onupdate="CASCADE",
    )


def downgrade():
    op.drop_constraint(
        "contextinclude_context_fkey",
        "context",
        type_="foreignkey"
    )
    op.drop_constraint(
        "contextinclude_include_fkey",
        "context",
        type_="foreignkey"
    )