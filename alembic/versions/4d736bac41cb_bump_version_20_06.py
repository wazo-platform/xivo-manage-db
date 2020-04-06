"""bump_version_20_06

Revision ID: 4d736bac41cb
Revises: fb663a210806

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d736bac41cb'
down_revision = 'fb663a210806'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='20.06'))


def downgrade():
    pass
