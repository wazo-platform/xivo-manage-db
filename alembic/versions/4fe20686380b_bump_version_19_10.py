"""bump_version_19_10

Revision ID: 4fe20686380b
Revises: 9b7e32eb0a77

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4fe20686380b'
down_revision = '9b7e32eb0a77'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='19.10'))


def downgrade():
    pass
