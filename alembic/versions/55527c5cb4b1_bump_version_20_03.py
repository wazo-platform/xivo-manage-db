"""bump_version_20_03

Revision ID: 55527c5cb4b1
Revises: 4722bbe519b1

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55527c5cb4b1'
down_revision = '4722bbe519b1'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='20.03'))


def downgrade():
    pass
