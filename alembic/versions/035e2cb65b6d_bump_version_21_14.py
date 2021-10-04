"""bump_version_21_14

Revision ID: 035e2cb65b6d
Revises: 37c0864e0b2b

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '035e2cb65b6d'
down_revision = '37c0864e0b2b'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='21.14'))


def downgrade():
    pass
