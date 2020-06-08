"""bump_version_20_09

Revision ID: d90ff200ae53
Revises: 06149af25f0d

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd90ff200ae53'
down_revision = '06149af25f0d'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='20.09'))


def downgrade():
    pass
