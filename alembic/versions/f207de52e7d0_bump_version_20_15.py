"""bump_version_20_15

Revision ID: f207de52e7d0
Revises: e5e53b7dc5d0

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f207de52e7d0'
down_revision = 'e5e53b7dc5d0'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='20.15'))


def downgrade():
    pass
