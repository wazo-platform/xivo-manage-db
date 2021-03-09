"""bump_version_21_04

Revision ID: 9442da3b20b6
Revises: 1583f90b21ad

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9442da3b20b6'
down_revision = '1583f90b21ad'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='21.04'))


def downgrade():
    pass
