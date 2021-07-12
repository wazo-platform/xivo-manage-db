"""bump_version_21_10

Revision ID: cb5666745311
Revises: 978e620de034

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb5666745311'
down_revision = '978e620de034'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='21.10'))


def downgrade():
    pass
