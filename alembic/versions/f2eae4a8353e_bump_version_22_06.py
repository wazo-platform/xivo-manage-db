"""bump_version_22_06

Revision ID: f2eae4a8353e
Revises: 2b65d248c2ad

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2eae4a8353e'
down_revision = '2b65d248c2ad'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='22.06'))


def downgrade():
    pass
