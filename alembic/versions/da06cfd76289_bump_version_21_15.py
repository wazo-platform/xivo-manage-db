"""bump_version_21_15

Revision ID: da06cfd76289
Revises: 12b81f6c229b

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da06cfd76289'
down_revision = '12b81f6c229b'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='21.15'))


def downgrade():
    pass
