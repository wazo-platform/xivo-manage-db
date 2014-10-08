"""group timeout may be null

Revision ID: 3096b11582cf
Revises: 4cf59c82b51e

"""

# revision identifiers, used by Alembic.
revision = '3096b11582cf'
down_revision = '4cf59c82b51e'

from alembic import op
import sqlalchemy as sa


groupfeatures_table = sa.sql.table('groupfeatures',
                                   sa.Column('timeout', sa.Integer))


def upgrade():
    op.alter_column('groupfeatures', 'timeout', server_default=None, nullable=True)


def downgrade():
    op.execute(groupfeatures_table.update().
               where(groupfeatures_table.c.timeout == None).
               values(timeout='0'))
    op.alter_column('groupfeatures', 'timeout', server_default='0', nullable=False)
