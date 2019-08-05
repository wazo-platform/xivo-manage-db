"""bump_version_19_12

Revision ID: 0a7363700618
Revises: 5047425b0f5c

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a7363700618'
down_revision = '5047425b0f5c'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='19.12'))


def downgrade():
    pass
