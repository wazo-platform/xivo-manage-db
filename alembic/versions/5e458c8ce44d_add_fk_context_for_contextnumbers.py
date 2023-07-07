"""add_fk_context_for_contextnumbers

Revision ID: 5e458c8ce44d
Revises: dbcec8abd7c1

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = '5e458c8ce44d'
down_revision = 'dbcec8abd7c1'


def upgrade():
    op.execute('DELETE FROM contextnumbers WHERE context NOT IN (SELECT DISTINCT name FROM context)')
    op.create_foreign_key(
        None,
        "contextnumbers",
        "context",
        ["context"],
        ["name"],
        ondelete="CASCADE"
    )


def downgrade():
    op.drop_constraint(
        "contextnumbers_context_fkey",
        "context",
        type_="foreignkey"
    )
