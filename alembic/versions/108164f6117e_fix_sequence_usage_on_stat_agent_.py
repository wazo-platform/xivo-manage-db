"""fix sequence usage on stat_agent_periodic

Revision ID: 108164f6117e
Revises: 52bd5977c09d
Create Date: 2014-05-09 09:17:37.551108
XiVO Version: 14.08

"""

# revision identifiers, used by Alembic.
revision = '108164f6117e'
down_revision = '52bd5977c09d'

from alembic import op


def upgrade():
    op.execute("SELECT setval('stat_agent_periodic_id_seq', (SELECT max(id) FROM stat_agent_periodic));")


def downgrade():
    pass
