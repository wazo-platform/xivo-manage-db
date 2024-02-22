"""bump_version_24_04

Revision ID: 06d67b2a9a5e
Revises: b65364a583d8

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06d67b2a9a5e'
down_revision = 'b65364a583d8'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='24.04'))


def downgrade():
    pass
