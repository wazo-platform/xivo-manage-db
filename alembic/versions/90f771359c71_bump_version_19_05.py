"""bump_version_19_05

Revision ID: 90f771359c71
Revises: 454c3dfde5db

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90f771359c71'
down_revision = '454c3dfde5db'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='19.05'))


def downgrade():
    pass
