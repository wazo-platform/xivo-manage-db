"""remove queue_info function

Revision ID: 241501a5f8ba
Revises: 203129d6b213

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = '241501a5f8ba'
down_revision = '203129d6b213'


def upgrade():
    op.get_bind().execute(
        'DROP FUNCTION IF EXISTS "get_queue_statistics" (text, int, int)'
    )


def downgrade():
    pass
