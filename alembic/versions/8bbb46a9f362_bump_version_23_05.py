"""bump_version_23_05

Revision ID: 8bbb46a9f362
Revises: f33878e11ef4

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8bbb46a9f362'
down_revision = 'f33878e11ef4'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='23.05'))


def downgrade():
    pass
