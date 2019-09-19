"""bump_version_19_14

Revision ID: 4d80d8106d1e
Revises: cbd383662cc0

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d80d8106d1e'
down_revision = 'cbd383662cc0'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='19.14'))


def downgrade():
    pass
