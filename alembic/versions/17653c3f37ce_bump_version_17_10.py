"""bump_version_17_10

Revision ID: 17653c3f37ce
Revises: fd040214cccb

"""

# revision identifiers, used by Alembic.
revision = '17653c3f37ce'
down_revision = 'fd040214cccb'

from alembic import op
import sqlalchemy as sa


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='17.10'))


def downgrade():
    pass
