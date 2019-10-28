"""bump_version_19_16

Revision ID: 449045080bf6
Revises: 8691b32cf44e

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '449045080bf6'
down_revision = '8691b32cf44e'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='19.16'))


def downgrade():
    pass
