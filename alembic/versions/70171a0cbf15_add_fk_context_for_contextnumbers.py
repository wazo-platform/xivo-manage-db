"""add_fk_context_for_contextnumbers

Revision ID: 70171a0cbf15
Revises: 85a827ab4711

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = '70171a0cbf15'
down_revision = '85a827ab4711'



def upgrade():
    op.create_foreign_key(
        None,
        "contextnumbers",
        "context",
        ["context"],
        ["name"],
        ondelete="CASCADE",
    )


def downgrade():
    op.drop_constraint(
        "contextnumbers_context_fkey",
        "context",
        type_="foreignkey"
    )
