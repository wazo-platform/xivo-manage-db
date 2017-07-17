"""bump_version_17_11

Revision ID: 60eb57605f3
Revises: bc9e62985a0

"""

# revision identifiers, used by Alembic.
revision = '60eb57605f3'
down_revision = 'bc9e62985a0'

from alembic import op
import sqlalchemy as sa


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='17.11'))


def downgrade():
    pass
