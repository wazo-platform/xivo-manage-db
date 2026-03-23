"""bump_version_26_05

Revision ID: f3bc803db64e
Revises: 0433093321f1

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = 'f3bc803db64e'
down_revision = '0433093321f1'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='26.05'))


def downgrade():
    pass
