"""bump_version_26_04

Revision ID: 517d371081d0
Revises: e01c44b679ed

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = '517d371081d0'
down_revision = 'e01c44b679ed'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='26.04'))


def downgrade():
    pass
