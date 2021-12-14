"""bump version to 22.01

Revision ID: 55cd08a0dae2
Revises: c04ed3f6a685

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55cd08a0dae2'
down_revision = 'c04ed3f6a685'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='22.01'))


def downgrade():
    pass
