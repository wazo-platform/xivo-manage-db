"""bump_version_20_02

Revision ID: 92061fe1c3b8
Revises: 0b694daf27e0

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92061fe1c3b8'
down_revision = '0b694daf27e0'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='20.02'))


def downgrade():
    pass
