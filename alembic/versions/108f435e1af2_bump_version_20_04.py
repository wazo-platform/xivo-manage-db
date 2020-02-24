"""bump_version_20_04

Revision ID: 108f435e1af2
Revises: 55527c5cb4b1

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '108f435e1af2'
down_revision = '55527c5cb4b1'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='20.04'))


def downgrade():
    pass
