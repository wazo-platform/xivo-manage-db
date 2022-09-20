"""bump_version_22_14

Revision ID: 7d342adb6ae1
Revises: f9ea1046c8e5

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d342adb6ae1'
down_revision = 'f9ea1046c8e5'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='22.14'))


def downgrade():
    pass
