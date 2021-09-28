"""convert agent_status_login to pjsip

Revision ID: 37c0864e0b2b
Revises: 42db6d46c98a

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37c0864e0b2b'
down_revision = '42db6d46c98a'

agent_login_status_tbl = sa.sql.table(
    'agent_login_status',
    sa.sql.column('state_interface'),
    sa.sql.column('interface'),
)


def upgrade():
    op.execute(
        agent_login_status_tbl
        .update()
        .where(agent_login_status_tbl.c.state_interface.startswith('SIP/'))
        .values(state_interface='PJ' + agent_login_status_tbl.c.state_interface)
    )
    op.execute(
        agent_login_status_tbl
        .update()
        .where(agent_login_status_tbl.c.interface.startswith('SIP/'))
        .values(interface='PJ' + agent_login_status_tbl.c.interface)
    )


def downgrade():
    pass
