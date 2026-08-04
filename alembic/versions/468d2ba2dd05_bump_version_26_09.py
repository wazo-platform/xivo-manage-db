"""bump_version_26_09

Revision ID: 468d2ba2dd05
Revises: 3f8c1de92a74

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = '468d2ba2dd05'
down_revision = '3f8c1de92a74'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='26.09'))


def downgrade():
    pass
