"""add_ondelete_cascade_fk_tenant

Revision ID: aecdd60623a1
Revises: 8fe383847bcc

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = 'aecdd60623a1'
down_revision = '8fe383847bcc'


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
