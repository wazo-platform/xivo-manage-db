"""add_fk_context_for_voicemail

Revision ID: 9869009eb5b3
Revises: c9b7c156e02a

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = '9869009eb5b3'
down_revision = 'c9b7c156e02a'




def upgrade():
    op.create_foreign_key(
        None,
        "voicemail",
        "context",
        ["context"],
        ["name"],
        ondelete="CASCADE",
    )


def downgrade():
    op.drop_constraint(
        "voicemail_context_fkey",
        "context",
        type_="foreignkey"
    )
