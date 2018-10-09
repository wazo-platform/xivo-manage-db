"""bump_version_18_12

Revision ID: 74a76197acaa
Revises: ce624f5d7fe2

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74a76197acaa'
down_revision = 'ce624f5d7fe2'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='18.12'))


def downgrade():
    pass
