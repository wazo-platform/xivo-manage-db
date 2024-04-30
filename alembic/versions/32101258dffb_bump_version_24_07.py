"""bump_version_24_07

Revision ID: 32101258dffb
Revises: cce0a44f44b1

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32101258dffb'
down_revision = 'cce0a44f44b1'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='24.07'))


def downgrade():
    pass
