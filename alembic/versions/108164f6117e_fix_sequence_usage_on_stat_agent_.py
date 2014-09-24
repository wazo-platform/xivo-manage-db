"""fix sequence usage on stat_agent_periodic

Revision ID: 108164f6117e
Revises: 52bd5977c09d

"""

# revision identifiers, used by Alembic.
revision = '108164f6117e'
down_revision = '52bd5977c09d'

from alembic import op


def upgrade():
    op.execute("SELECT setval('stat_agent_periodic_id_seq', (SELECT max(id) FROM stat_agent_periodic));")


def downgrade():
    pass
