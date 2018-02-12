"""bump_version_18_03

Revision ID: 41a523e18fdd
Revises: 36516503ae1b

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41a523e18fdd'
down_revision = '36516503ae1b'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='18.03'))


def downgrade():
    pass
