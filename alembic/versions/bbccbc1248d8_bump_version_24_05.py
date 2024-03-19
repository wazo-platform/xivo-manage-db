"""bump_version_24_05

Revision ID: bbccbc1248d8
Revises: 40c244ac9a97

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bbccbc1248d8'
down_revision = '40c244ac9a97'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='24.05'))


def downgrade():
    pass
