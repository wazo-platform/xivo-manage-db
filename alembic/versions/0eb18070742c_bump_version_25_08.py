"""bump_version_25_08

Revision ID: 0eb18070742c
Revises: e4209e4e9522

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = '0eb18070742c'
down_revision = 'e4209e4e9522'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='25.08'))


def downgrade():
    pass
