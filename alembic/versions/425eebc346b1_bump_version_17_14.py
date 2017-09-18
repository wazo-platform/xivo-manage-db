"""bump_version_17_14

Revision ID: 425eebc346b1
Revises: 3e7dbde01837

"""

# revision identifiers, used by Alembic.
revision = '425eebc346b1'
down_revision = '3e7dbde01837'

from alembic import op
import sqlalchemy as sa


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='17.14'))


def downgrade():
    pass
