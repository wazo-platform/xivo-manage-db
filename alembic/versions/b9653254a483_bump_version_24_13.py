"""bump_version_24_13

Revision ID: b9653254a483
Revises: 1fd612522db7

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9653254a483'
down_revision = '1fd612522db7'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='24.13'))


def downgrade():
    pass
