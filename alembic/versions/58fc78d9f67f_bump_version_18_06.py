"""bump_version_18_06

Revision ID: 58fc78d9f67f
Revises: 3a091c2f91bc

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58fc78d9f67f'
down_revision = '3a091c2f91bc'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='18.06'))


def downgrade():
    pass
