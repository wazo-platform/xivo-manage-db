"""bump_version_22_12

Revision ID: 0600c04fd4a6
Revises: a46c624e7f61

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0600c04fd4a6'
down_revision = 'a46c624e7f61'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='22.12'))


def downgrade():
    pass
