"""bump_version_17_13

Revision ID: 3e7dbde01837
Revises: 508c5a0382dc

"""

# revision identifiers, used by Alembic.
revision = '3e7dbde01837'
down_revision = '508c5a0382dc'

from alembic import op
import sqlalchemy as sa


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='17.13'))


def downgrade():
    pass
