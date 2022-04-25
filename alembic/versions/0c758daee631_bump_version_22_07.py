"""bump_version_22_07

Revision ID: 0c758daee631
Revises: f2eae4a8353e

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c758daee631'
down_revision = 'f2eae4a8353e'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='22.07'))


def downgrade():
    pass
