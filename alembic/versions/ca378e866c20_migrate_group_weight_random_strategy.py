"""migrate group weight random strategy

Revision ID: ca378e866c20
Revises: c6a2fbdd654a

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'ca378e866c20'
down_revision = 'c6a2fbdd654a'

queue_table = sa.sql.table(
    'queue',
    sa.sql.column('category'),
    sa.sql.column('strategy'),
)


def upgrade():
    # group members have no penalty, so wrandom already behaved like random
    op.execute(
        queue_table.update()
        .where(queue_table.c.category == 'group')
        .where(queue_table.c.strategy == 'wrandom')
        .values(strategy='random')
    )


def downgrade():
    pass
