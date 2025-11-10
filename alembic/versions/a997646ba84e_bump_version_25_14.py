"""bump_version_25_14

Revision ID: a997646ba84e
Revises: c17681419c6e

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = 'a997646ba84e'
down_revision = None


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='25.14'))


def downgrade():
    pass
