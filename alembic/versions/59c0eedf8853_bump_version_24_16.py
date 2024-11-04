"""bump_version_24_16

Revision ID: 59c0eedf8853
Revises: d80c07b01d39

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59c0eedf8853'
down_revision = 'd80c07b01d39'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='24.16'))


def downgrade():
    pass
