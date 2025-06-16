"""add agent-membership-status fk

Revision ID: 17f66360ee2f
Revises: 3131b2ccb06f

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = '17f66360ee2f'
down_revision = '3131b2ccb06f'


def upgrade():
    op.create_foreign_key(
        None,
        "agent_membership_status",
        "agentfeatures",
        ["agent_id"],
        ["id"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        None,
        "agent_membership_status",
        "queuefeatures",
        ["queue_id"],
        ["id"],
        ondelete="CASCADE",
    )


def downgrade():
    op.drop_constraint(
        "agent_membership_status_queue_id_fkey",
        "agent_membership_status",
        type_="foreignkey",
    )
    op.drop_constraint(
        "agent_membership_status_agent_id_fkey",
        "agent_membership_status",
        type_="foreignkey",
    )
