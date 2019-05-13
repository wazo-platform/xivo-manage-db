"""bump_version_19_08

Revision ID: 4c1cbf778770
Revises: 15ca57fa1b71

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c1cbf778770'
down_revision = '15ca57fa1b71'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='19.08'))


def downgrade():
    pass
