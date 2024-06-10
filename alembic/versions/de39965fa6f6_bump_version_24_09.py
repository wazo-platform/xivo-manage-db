"""bump_version_24_09

Revision ID: de39965fa6f6
Revises: a805579d911f

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de39965fa6f6'
down_revision = 'a805579d911f'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='24.09'))


def downgrade():
    pass
