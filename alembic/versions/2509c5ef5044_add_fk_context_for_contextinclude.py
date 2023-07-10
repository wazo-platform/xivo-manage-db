"""add_fk_context_for_contextinclude

Revision ID: 2509c5ef5044
Revises: 5e458c8ce44d

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = '2509c5ef5044'
down_revision = '5e458c8ce44d'


def upgrade():
    op.execute('DELETE FROM contextinclude WHERE context NOT IN (SELECT DISTINCT name FROM context)')
    op.create_foreign_key(
        None,
        "contextinclude",
        "context",
        ["context"],
        ["name"],
        ondelete="CASCADE"
    )


def downgrade():
    op.drop_constraint(
        "contextinclude_context_fkey",
        "contextinclude",
        type_="foreignkey"
    )
