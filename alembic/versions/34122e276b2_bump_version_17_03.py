"""bump_version_17_03

Revision ID: 34122e276b2
Revises: c3b40a0998c4

"""

# revision identifiers, used by Alembic.
revision = '34122e276b2'
down_revision = 'c3b40a0998c4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='17.03'))


def downgrade():
    pass
