"""add_ondelete_cascade_fk_tenant

Revision ID: c9b7c156e02a
Revises: 8675398b047b

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = 'c9b7c156e02a'
down_revision = '8675398b047b'


def upgrade():
    op.drop_constraint("context_tenant_uuid_fkey", "context", type_="foreignkey")
    op.create_foreign_key(
        None,
        "context",
        "tenant",
        ["tenant_uuid"],
        ["uuid"],
        ondelete="CASCADE",
    )


def downgrade():
    op.drop_constraint("context_tenant_uuid_fkey", "context", type_="foreignkey")
    op.create_foreign_key(
        None,
        "context",
        "tenant",
        ["tenant_uuid"],
        ["uuid"]
    )