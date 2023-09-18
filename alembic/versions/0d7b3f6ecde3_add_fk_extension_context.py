"""add_fk_extension_context

Revision ID: 0d7b3f6ecde3
Revises: 71a9a51925d0

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = '0d7b3f6ecde3'
down_revision = '71a9a51925d0'


def upgrade():
    op.execute(
        'DELETE FROM extensions WHERE context NOT IN (SELECT DISTINCT name FROM context)'
    )
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
