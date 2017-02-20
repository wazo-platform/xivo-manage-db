"""bump_version_17_04

Revision ID: 37b9ac945437
Revises: 415b08ed9959

"""

# revision identifiers, used by Alembic.
revision = '37b9ac945437'
down_revision = '415b08ed9959'

from alembic import op
import sqlalchemy as sa


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='17.04'))


def downgrade():
    pass
