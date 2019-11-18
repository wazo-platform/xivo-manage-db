"""bump_version_19_17

Revision ID: 4c4a8eaa31e7
Revises: 449045080bf6

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c4a8eaa31e7'
down_revision = '449045080bf6'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='19.17'))


def downgrade():
    pass
