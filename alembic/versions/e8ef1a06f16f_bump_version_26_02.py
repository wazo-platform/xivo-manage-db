"""bump_version_26_02

Revision ID: e8ef1a06f16f
Revises: fb097e414392

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = 'e8ef1a06f16f'
down_revision = 'fb097e414392'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='26.02'))


def downgrade():
    pass
