"""bump_version_18_01

Revision ID: 40359c5c2c92
Revises: 1815dcbc813f

"""

# revision identifiers, used by Alembic.
revision = '40359c5c2c92'
down_revision = '1815dcbc813f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='18.01'))


def downgrade():
    pass
