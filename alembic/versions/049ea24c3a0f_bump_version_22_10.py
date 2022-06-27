"""bump_version_22_10

Revision ID: 049ea24c3a0f
Revises: 7541da6ac48f

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '049ea24c3a0f'
down_revision = '7541da6ac48f'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='22.10'))


def downgrade():
    pass
