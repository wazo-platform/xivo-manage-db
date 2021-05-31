"""bump_version_21_08

Revision ID: 9eeb96b396a7
Revises: 2b5d68fa7ab8

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9eeb96b396a7'
down_revision = '2b5d68fa7ab8'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='21.08'))


def downgrade():
    pass
