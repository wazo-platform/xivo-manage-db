"""bump_version_18_05

Revision ID: 52acaaba550c
Revises: 4a5a1c3eb52f

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52acaaba550c'
down_revision = '4a5a1c3eb52f'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='18.05'))


def downgrade():
    pass
