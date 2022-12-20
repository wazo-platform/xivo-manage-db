"""bump_version_23_01

Revision ID: c8415eb8bfb5
Revises: 1108308b3fd7

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8415eb8bfb5'
down_revision = '1108308b3fd7'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='23.01'))


def downgrade():
    pass
