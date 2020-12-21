"""bump_version_21_01

Revision ID: 2bb55c201ee7
Revises: b1dfaf771da8

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2bb55c201ee7'
down_revision = 'b1dfaf771da8'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='21.01'))


def downgrade():
    pass
