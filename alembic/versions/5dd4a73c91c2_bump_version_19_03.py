"""bump_version_19_03

Revision ID: 5dd4a73c91c2
Revises: d81a903b6d1e

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5dd4a73c91c2'
down_revision = 'd81a903b6d1e'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='19.03'))


def downgrade():
    pass
