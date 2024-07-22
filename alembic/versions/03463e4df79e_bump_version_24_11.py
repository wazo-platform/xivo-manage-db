"""bump_version_24_11

Revision ID: 03463e4df79e
Revises: 442b09d80585

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03463e4df79e'
down_revision = '442b09d80585'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='24.11'))


def downgrade():
    pass
