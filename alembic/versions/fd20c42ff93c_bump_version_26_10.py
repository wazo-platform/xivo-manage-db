"""bump_version_26_10

Revision ID: fd20c42ff93c
Revises: 468d2ba2dd05

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = 'fd20c42ff93c'
down_revision = '468d2ba2dd05'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='26.10'))


def downgrade():
    pass
