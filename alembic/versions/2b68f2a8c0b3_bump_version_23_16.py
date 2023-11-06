"""bump_version_23_16

Revision ID: 2b68f2a8c0b3
Revises: 91b9efd85e0b

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b68f2a8c0b3'
down_revision = '91b9efd85e0b'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='23.16'))


def downgrade():
    pass
