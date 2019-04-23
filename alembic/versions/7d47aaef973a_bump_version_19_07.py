"""bump_version_19_07

Revision ID: 7d47aaef973a
Revises: 9b0892a818e6

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d47aaef973a'
down_revision = '9b0892a818e6'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='19.07'))


def downgrade():
    pass
