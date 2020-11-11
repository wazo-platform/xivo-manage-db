"""bump_version_20_16

Revision ID: b1c4be6f46ff
Revises: 2796b8c839c5

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1c4be6f46ff'
down_revision = '2796b8c839c5'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='20.16'))


def downgrade():
    pass
