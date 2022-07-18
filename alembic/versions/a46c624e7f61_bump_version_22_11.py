"""bump_version_22_11

Revision ID: a46c624e7f61
Revises: 049ea24c3a0f

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a46c624e7f61'
down_revision = '049ea24c3a0f'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='22.11'))


def downgrade():
    pass
