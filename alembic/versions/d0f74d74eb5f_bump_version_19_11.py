"""bump_version_19_11

Revision ID: d0f74d74eb5f
Revises: 17ea1bc19d64

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0f74d74eb5f'
down_revision = '17ea1bc19d64'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='19.11'))


def downgrade():
    pass
