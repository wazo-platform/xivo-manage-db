"""divide queue waitratio

Revision ID: 3770e116222d
Revises: 2375157ea682

"""

# revision identifiers, used by Alembic.
revision = '3770e116222d'
down_revision = '2375157ea682'

from alembic import op
from sqlalchemy import sql


queuefeatures = sql.table('queuefeatures',
    sql.column('waitratio'),
)


def upgrade():
    op.execute(
        queuefeatures.update()
        .where(queuefeatures.c.waitratio != None)
        .values(waitratio=queuefeatures.c.waitratio / 100.0)
    )


def downgrade():
    op.execute(
        queuefeatures.update()
        .where(queuefeatures.c.waitratio != None)
        .values(waitratio=queuefeatures.c.waitratio * 100.0)
    )
