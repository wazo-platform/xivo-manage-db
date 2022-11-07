"""bump_version_22_16

Revision ID: b0edbcc1426d
Revises: e04b80f8b6fc

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0edbcc1426d'
down_revision = 'e04b80f8b6fc'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='22.16'))


def downgrade():
    pass
