"""bump_version_22_13

Revision ID: e53b8ab083c0
Revises: 0600c04fd4a6

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e53b8ab083c0'
down_revision = '0600c04fd4a6'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='22.13'))


def downgrade():
    pass
