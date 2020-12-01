"""bump_version_20_17

Revision ID: b62e1eba7869
Revises: 2f354a1653fc

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b62e1eba7869'
down_revision = '2f354a1653fc'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='20.17'))


def downgrade():
    pass
