"""bump_version_18_07

Revision ID: 34748356e196
Revises: b5c40615bc21

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34748356e196'
down_revision = 'b5c40615bc21'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='18.07'))


def downgrade():
    pass
