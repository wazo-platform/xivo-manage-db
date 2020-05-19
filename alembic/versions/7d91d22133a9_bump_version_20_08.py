"""bump_version_20_08

Revision ID: 7d91d22133a9
Revises: 2a27e01c8070

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d91d22133a9'
down_revision = '2a27e01c8070'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='20.08'))


def downgrade():
    pass
