"""bump_version_21_16

Revision ID: ce76c220eaab
Revises: 61e3d7c65755

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce76c220eaab'
down_revision = '61e3d7c65755'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='21.16'))


def downgrade():
    pass
