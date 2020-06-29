"""bump_version_20_10

Revision ID: eddc1df1d57c
Revises: 5600ad4c00b4

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eddc1df1d57c'
down_revision = '5600ad4c00b4'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='20.10'))


def downgrade():
    pass
