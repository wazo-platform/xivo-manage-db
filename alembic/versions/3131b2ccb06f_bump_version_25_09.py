"""bump_version_25_09

Revision ID: 3131b2ccb06f
Revises: aa8651c694fc

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = '3131b2ccb06f'
down_revision = 'aa8651c694fc'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='25.09'))


def downgrade():
    pass
