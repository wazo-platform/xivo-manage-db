"""bump_version_21_07

Revision ID: 2b5d68fa7ab8
Revises: 060e2360612f

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b5d68fa7ab8'
down_revision = '060e2360612f'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='21.07'))


def downgrade():
    pass
