"""bump_version_17_09

Revision ID: 13472f54a7
Revises: b57ed1e30535

"""

# revision identifiers, used by Alembic.
revision = '13472f54a7'
down_revision = 'b57ed1e30535'

from alembic import op
import sqlalchemy as sa


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='17.09'))


def downgrade():
    pass
