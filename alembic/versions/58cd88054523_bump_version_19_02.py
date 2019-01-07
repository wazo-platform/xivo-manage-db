"""bump_version_19_02

Revision ID: 58cd88054523
Revises: b6a0f4cc7e49

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58cd88054523'
down_revision = 'b6a0f4cc7e49'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='19.02'))


def downgrade():
    pass
