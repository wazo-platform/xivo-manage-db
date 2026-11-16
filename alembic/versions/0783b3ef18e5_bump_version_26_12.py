"""bump_version_26_12

Revision ID: 0783b3ef18e5
Revises: ca378e866c20

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = '0783b3ef18e5'
down_revision = 'ca378e866c20'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='26.12'))


def downgrade():
    pass
