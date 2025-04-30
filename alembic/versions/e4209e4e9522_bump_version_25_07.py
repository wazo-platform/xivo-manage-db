"""bump_version_25_07

Revision ID: e4209e4e9522
Revises: 4e6562f15b59

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = 'e4209e4e9522'
down_revision = '4e6562f15b59'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='25.07'))


def downgrade():
    pass
