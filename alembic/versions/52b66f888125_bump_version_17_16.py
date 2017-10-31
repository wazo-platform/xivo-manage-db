"""bump_version_17_16

Revision ID: 52b66f888125
Revises: 10bf9a42edee

"""

# revision identifiers, used by Alembic.
revision = '52b66f888125'
down_revision = '10bf9a42edee'

from alembic import op
import sqlalchemy as sa


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='17.16'))


def downgrade():
    pass
