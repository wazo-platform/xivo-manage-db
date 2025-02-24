"""bump_version_25_04

Revision ID: 9485e1dae58c
Revises: 5a1349bd2ab0

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = '9485e1dae58c'
down_revision = '5a1349bd2ab0'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='25.04'))


def downgrade():
    pass
