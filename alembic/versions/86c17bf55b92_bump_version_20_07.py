"""bump_version_20_07

Revision ID: 86c17bf55b92
Revises: 2a24c3d1d13e

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86c17bf55b92'
down_revision = '2a24c3d1d13e'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='20.07'))


def downgrade():
    pass
