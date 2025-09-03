"""bump_version_25_13

Revision ID: c17681419c6e
Revises: d11fa04f371c

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = 'c17681419c6e'
down_revision = 'd11fa04f371c'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='25.13'))


def downgrade():
    pass
