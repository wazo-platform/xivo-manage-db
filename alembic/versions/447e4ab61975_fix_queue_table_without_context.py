"""fix_queue_table_without_context

Revision ID: 447e4ab61975
Revises: 146ddf6c4b36

"""

# revision identifiers, used by Alembic.
revision = '447e4ab61975'
down_revision = '146ddf6c4b36'

from alembic import op
from sqlalchemy.sql import table, column
from sqlalchemy import String


def upgrade():
    qry = """UPDATE queue SET context = queuefeatures.context from queuefeatures WHERE queuefeatures.name = queue.name"""
    op.execute(qry)
    qry = """UPDATE queue SET context = groupfeatures.context from groupfeatures WHERE groupfeatures.name = queue.name"""
    op.execute(qry)


def downgrade():
    queue = table('queue',
        column('context', String)
    )
    op.execute(
        queue.update().values({'context': ''})
    )
