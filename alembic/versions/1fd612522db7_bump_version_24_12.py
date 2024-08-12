"""bump_version_24_12

Revision ID: 1fd612522db7
Revises: 439de3c2f1ae

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fd612522db7'
down_revision = '439de3c2f1ae'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='24.12'))


def downgrade():
    pass
