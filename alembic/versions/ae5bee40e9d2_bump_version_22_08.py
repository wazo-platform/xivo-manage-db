"""bump_version_22_08

Revision ID: ae5bee40e9d2
Revises: 0c758daee631

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae5bee40e9d2'
down_revision = '0c758daee631'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='22.08'))


def downgrade():
    pass
