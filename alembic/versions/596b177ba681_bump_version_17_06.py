"""bump_version_17_06

Revision ID: 596b177ba681
Revises: 4e07e476eb0b

"""

# revision identifiers, used by Alembic.
revision = '596b177ba681'
down_revision = '4e07e476eb0b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='17.06'))


def downgrade():
    pass
