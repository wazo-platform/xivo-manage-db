"""bump_version_24_14

Revision ID: c55e390ac48c
Revises: b9653254a483

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c55e390ac48c'
down_revision = 'b9653254a483'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='24.14'))


def downgrade():
    pass
