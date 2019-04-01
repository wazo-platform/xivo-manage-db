"""bump_version_19_06

Revision ID: 87b36150b613
Revises: 1192e6bfd226

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87b36150b613'
down_revision = '1192e6bfd226'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='19.06'))


def downgrade():
    pass
