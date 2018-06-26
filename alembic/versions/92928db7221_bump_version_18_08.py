"""bump_version_18_08

Revision ID: 92928db7221
Revises: c193f30636ff

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92928db7221'
down_revision = 'c193f30636ff'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='18.08'))


def downgrade():
    pass
