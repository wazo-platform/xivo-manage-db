"""bump_version_18_11

Revision ID: 0d74d34f7782
Revises: 47920341f392

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d74d34f7782'
down_revision = '47920341f392'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='18.11'))


def downgrade():
    pass
