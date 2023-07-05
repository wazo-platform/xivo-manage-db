"""add_fk_context_for_contextmember

Revision ID: dbcec8abd7c1
Revises: aecdd60623a1

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = 'dbcec8abd7c1'
down_revision = 'aecdd60623a1'


def upgrade():
    op.execute('DELETE FROM contextmember WHERE context NOT IN (SELECT DISTINCT name FROM context)')
    op.create_foreign_key(
        None,
        "contextmember",
        "context",
        ["context"],
        ["name"],
        ondelete="CASCADE",
        onupdate="CASCADE",
    )


def downgrade():
    op.drop_constraint(
        "contextmember_context_fkey",
        "context",
        type_="foreignkey")
