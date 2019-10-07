"""bump_version_19_15

Revision ID: 732a9b6500da
Revises: 5faf5386dca8

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '732a9b6500da'
down_revision = '5faf5386dca8'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='19.15'))


def downgrade():
    pass
