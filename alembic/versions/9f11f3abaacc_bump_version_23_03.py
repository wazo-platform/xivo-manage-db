"""bump_version_23_03

Revision ID: 9f11f3abaacc
Revises: 1264fdcb3e71

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f11f3abaacc'
down_revision = '1264fdcb3e71'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='23.03'))


def downgrade():
    pass
