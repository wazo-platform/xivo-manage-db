"""bump_version_20_13

Revision ID: 4aa03039dd2e
Revises: d56d7434e9f4

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4aa03039dd2e'
down_revision = 'd56d7434e9f4'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='20.13'))


def downgrade():
    pass
