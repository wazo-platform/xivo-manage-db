"""bump_version_25_02

Revision ID: 00ae4937814f
Revises: a2541348bcae

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00ae4937814f'
down_revision = 'a2541348bcae'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='25.02'))


def downgrade():
    pass
