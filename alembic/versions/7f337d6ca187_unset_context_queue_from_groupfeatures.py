"""unset_context_queue_from_groupfeatures

Revision ID: 7f337d6ca187
Revises: c8abcc5497ef

"""

from alembic import op
from sqlalchemy import sql

# revision identifiers, used by Alembic.
revision = '7f337d6ca187'
down_revision = 'c8abcc5497ef'

queue_tbl = sql.table(
    'queue',
    sql.column('category'),
    sql.column('context'),
)


def upgrade():
    op.execute(
        queue_tbl.update()
        .where(queue_tbl.c.category == 'group')
        .values(context=None)
    )


def downgrade():
    pass
