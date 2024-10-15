"""bump_version_24_15

Revision ID: 75212659ab23
Revises: 42f9334e4f25

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75212659ab23'
down_revision = '42f9334e4f25'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='24.15'))


def downgrade():
    pass
