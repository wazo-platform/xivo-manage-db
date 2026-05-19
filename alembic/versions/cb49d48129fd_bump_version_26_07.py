"""bump_version_26_07

Revision ID: cb49d48129fd
Revises: 0dd9e46ce2bc

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = 'cb49d48129fd'
down_revision = '0dd9e46ce2bc'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='26.07'))


def downgrade():
    pass
