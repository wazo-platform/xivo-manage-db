"""bump_version_19_09

Revision ID: 9b7e32eb0a77
Revises: cac9af37c973

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b7e32eb0a77'
down_revision = 'cac9af37c973'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='19.09'))


def downgrade():
    pass
