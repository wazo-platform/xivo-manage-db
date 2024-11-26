"""bump_version_24_17

Revision ID: 710bfcfde4bd
Revises: b8a823cde2fc

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '710bfcfde4bd'
down_revision = 'b8a823cde2fc'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='24.17'))


def downgrade():
    pass
