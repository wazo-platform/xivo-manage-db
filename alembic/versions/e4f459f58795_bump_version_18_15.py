"""bump_version_18_15

Revision ID: e4f459f58795
Revises: 1311cd6c2a63

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4f459f58795'
down_revision = '1311cd6c2a63'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='18.15'))


def downgrade():
    pass
