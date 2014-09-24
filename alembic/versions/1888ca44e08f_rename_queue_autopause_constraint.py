"""rename queue autopause constraint

Revision ID: 1888ca44e08f
Revises: 50cfb10bd01d

"""

# revision identifiers, used by Alembic.
revision = '1888ca44e08f'
down_revision = '50cfb10bd01d'

from alembic import op

drop_query = "ALTER TABLE queue DROP CONSTRAINT IF EXISTS {name}"

add_query = """
    ALTER TABLE queue
    ADD CONSTRAINT {name}
        CHECK (autopause IN ('no','yes','all'))
"""


def upgrade():
    op.execute(drop_query.format(name='queue_autopause'))
    op.execute(drop_query.format(name='queue_autopause_check'))
    op.execute(add_query.format(name='queue_autopause_check'))


def downgrade():
    op.execute(drop_query.format(name='queue_autopause'))
    op.execute(drop_query.format(name='queue_autopause_check'))
    op.execute(add_query.format(name='queue_autopause'))
