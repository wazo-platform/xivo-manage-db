"""bump_version_22_17

Revision ID: 1108308b3fd7
Revises: b0edbcc1426d

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1108308b3fd7'
down_revision = 'b0edbcc1426d'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='22.17'))


def downgrade():
    pass
