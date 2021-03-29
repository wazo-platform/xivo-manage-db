"""bump_version_21_05

Revision ID: e6c5e0410e89
Revises: 4d539700bb90

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6c5e0410e89'
down_revision = '4d539700bb90'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='21.05'))


def downgrade():
    pass
