"""bump_version_25_12

Revision ID: d11fa04f371c
Revises: b425ccca8dce

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = 'd11fa04f371c'
down_revision = 'b425ccca8dce'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='25.12'))


def downgrade():
    pass
