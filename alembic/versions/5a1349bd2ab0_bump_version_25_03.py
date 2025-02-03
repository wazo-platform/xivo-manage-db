"""bump_version_25_03

Revision ID: 5a1349bd2ab0
Revises: 3d1087b7867b

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = '5a1349bd2ab0'
down_revision = '3d1087b7867b'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='25.03'))


def downgrade():
    pass
