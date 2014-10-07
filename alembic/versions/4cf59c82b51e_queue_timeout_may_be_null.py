"""queue timeout may be null

Revision ID: 4cf59c82b51e
Revises: 234745874c55

"""

# revision identifiers, used by Alembic.
revision = '4cf59c82b51e'
down_revision = '234745874c55'

from alembic import op
import sqlalchemy as sa

queuefeatures_table = sa.sql.table('queuefeatures',
                                   sa.Column('timeout', sa.Integer))


def upgrade():
    op.alter_column('queuefeatures', 'timeout', server_default=None, nullable=True)


def downgrade():
    op.execute(queuefeatures_table.update().
               where(queuefeatures_table.c.timeout == None).
               values(timeout='0'))
    op.alter_column('queuefeatures', 'timeout', server_default='0', nullable=False)
