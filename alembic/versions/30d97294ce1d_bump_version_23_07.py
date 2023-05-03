"""bump_version_23_07

Revision ID: 30d97294ce1d
Revises: e507e100aa92

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30d97294ce1d'
down_revision = 'e507e100aa92'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='23.07'))


def downgrade():
    pass
