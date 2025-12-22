"""bump_version_26_01

Revision ID: fb097e414392
Revises: 2267d234ccd1

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = 'fb097e414392'
down_revision = '2267d234ccd1'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='26.01'))


def downgrade():
    pass
