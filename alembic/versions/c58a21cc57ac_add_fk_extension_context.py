"""add_fk_extension_context

Revision ID: c58a21cc57ac
Revises: b4fb4eb3cf8e

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = 'c58a21cc57ac'
down_revision = 'b4fb4eb3cf8e'


def upgrade():
    op.execute('DELETE FROM extensions WHERE context NOT IN (SELECT DISTINCT name FROM context)')
    op.create_foreign_key(
        None,
        "extensions",
        "context",
        ["context"],
        ["name"],
        ondelete="CASCADE",
    )


def downgrade():
    op.drop_constraint("extensions_context_fkey", "extensions", type_="foreignkey")
