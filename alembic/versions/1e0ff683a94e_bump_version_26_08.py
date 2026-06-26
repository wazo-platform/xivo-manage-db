"""bump_version_26_08

Revision ID: 1e0ff683a94e
Revises: d55959673959

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = '1e0ff683a94e'
down_revision = 'd55959673959'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='26.08'))


def downgrade():
    pass
