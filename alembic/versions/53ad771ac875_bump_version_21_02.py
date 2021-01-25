"""bump_version_21_02

Revision ID: 53ad771ac875
Revises: a10db8de6372

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53ad771ac875'
down_revision = 'a10db8de6372'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='21.02'))


def downgrade():
    pass
