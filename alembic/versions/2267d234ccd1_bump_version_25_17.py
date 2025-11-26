"""bump_version_25_17

Revision ID: 2267d234ccd1
Revises: f0046ed0d70e

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = '2267d234ccd1'
down_revision = 'f0046ed0d70e'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='25.17'))


def downgrade():
    pass
