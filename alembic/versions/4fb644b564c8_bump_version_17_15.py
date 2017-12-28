"""bump_version_17_15

Revision ID: 4fb644b564c8
Revises: 412b6135f650

"""

# revision identifiers, used by Alembic.
revision = '4fb644b564c8'
down_revision = '412b6135f650'

from alembic import op
import sqlalchemy as sa


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='17.15'))


def downgrade():
    pass
