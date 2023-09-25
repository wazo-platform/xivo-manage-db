"""bump_version_23_14

Revision ID: 30c3152833be
Revises: ee2692520bd4

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30c3152833be'
down_revision = 'ee2692520bd4'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='23.14'))


def downgrade():
    pass
