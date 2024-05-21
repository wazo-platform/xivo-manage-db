"""bump_version_24_08

Revision ID: 65b4ba443641
Revises: 32101258dffb

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65b4ba443641'
down_revision = '32101258dffb'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='24.08'))


def downgrade():
    pass
