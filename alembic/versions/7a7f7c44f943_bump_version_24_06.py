"""bump_version_24_06

Revision ID: 7a7f7c44f943
Revises: bbccbc1248d8

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a7f7c44f943'
down_revision = 'bbccbc1248d8'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='24.06'))


def downgrade():
    pass
