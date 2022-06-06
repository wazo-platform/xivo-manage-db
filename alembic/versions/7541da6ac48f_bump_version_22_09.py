"""bump_version_22_09

Revision ID: 7541da6ac48f
Revises: ae5bee40e9d2

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7541da6ac48f'
down_revision = 'ae5bee40e9d2'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='22.09'))


def downgrade():
    pass
