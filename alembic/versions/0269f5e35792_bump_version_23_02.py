"""bump_version_23_02

Revision ID: 0269f5e35792
Revises: c8415eb8bfb5

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0269f5e35792'
down_revision = 'c8415eb8bfb5'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='23.02'))


def downgrade():
    pass
