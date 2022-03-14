"""bump_version_22_05

Revision ID: 21b72c41eb6a
Revises: 0ffacfab7041

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21b72c41eb6a'
down_revision = '0ffacfab7041'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='22.05'))


def downgrade():
    pass
