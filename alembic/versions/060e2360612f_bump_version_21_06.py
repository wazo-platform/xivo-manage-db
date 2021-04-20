"""bump_version_21_06

Revision ID: 060e2360612f
Revises: 0f4a7c48613c

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '060e2360612f'
down_revision = '0f4a7c48613c'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='21.06'))


def downgrade():
    pass
