"""bump_version_17_08

Revision ID: 3612e8058d92
Revises: 3e6bc9ae6158

"""

# revision identifiers, used by Alembic.
revision = '3612e8058d92'
down_revision = '3e6bc9ae6158'

from alembic import op
import sqlalchemy as sa


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='17.08'))


def downgrade():
    pass
