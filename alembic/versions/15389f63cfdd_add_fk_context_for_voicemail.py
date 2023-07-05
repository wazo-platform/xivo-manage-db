"""add_fk_context_for_voicemail

Revision ID: 15389f63cfdd
Revises: 8fe383847bcc

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = '15389f63cfdd'
down_revision = '91d6933efd3e'


def upgrade():
    op.create_foreign_key(
        None,
        "voicemail",
        "context",
        ["context"],
        ["name"],
        ondelete="CASCADE",
        onupdate="CASCADE",
    )


def downgrade():
    op.drop_constraint(
        "voicemail_context_fkey",
        "context",
        type_="foreignkey"
    )
