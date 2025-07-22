"""bump_version_25_11

Revision ID: b425ccca8dce
Revises: 33f894a5a977

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = 'b425ccca8dce'
down_revision = '33f894a5a977'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='25.11'))


def downgrade():
    pass
