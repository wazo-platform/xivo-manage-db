"""remove orphaned agent status rows

Revision ID: 3f8c1de92a74
Revises: 1e0ff683a94e

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '3f8c1de92a74'
down_revision = '1e0ff683a94e'

agentfeatures_table = sa.sql.table(
    'agentfeatures',
    sa.sql.column('id'),
)

agent_login_status_table = sa.sql.table(
    'agent_login_status',
    sa.sql.column('agent_id'),
)

agent_membership_status_table = sa.sql.table(
    'agent_membership_status',
    sa.sql.column('agent_id'),
)


def upgrade():
    conn = op.get_bind()

    existing_agent_ids = sa.select([agentfeatures_table.c.id])

    conn.execute(
        agent_login_status_table.delete().where(
            agent_login_status_table.c.agent_id.notin_(existing_agent_ids)
        )
    )
    conn.execute(
        agent_membership_status_table.delete().where(
            agent_membership_status_table.c.agent_id.notin_(existing_agent_ids)
        )
    )


def downgrade():
    pass
