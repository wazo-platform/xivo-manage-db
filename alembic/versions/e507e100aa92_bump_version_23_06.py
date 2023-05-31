"""bump_version_23_06

Revision ID: e507e100aa92
Revises: None

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e507e100aa92'
down_revision = None


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='23.06'))


def downgrade():
    pass
