"""bump_version_25_10

Revision ID: ca4bca36b8ac
Revises: 3131b2ccb06f

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = 'ca4bca36b8ac'
down_revision = '3131b2ccb06f'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='25.10'))


def downgrade():
    pass
