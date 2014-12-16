"""reset queue exit context

Revision ID: 3ab28f25de30
Revises: 3770e116222d

"""

# revision identifiers, used by Alembic.
revision = '3ab28f25de30'
down_revision = '39f7b89af84e'

from alembic import op


def upgrade():
    op.execute('''UPDATE queue SET context = null FROM queuefeatures WHERE queue.name = queuefeatures.name AND queue.context = queuefeatures.context''')
    op.execute('''UPDATE queue SET context = null FROM groupfeatures WHERE queue.name = groupfeatures.name AND queue.context = groupfeatures.context''')


def downgrade():
    pass
