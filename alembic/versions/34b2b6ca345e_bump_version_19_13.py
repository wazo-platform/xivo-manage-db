"""bump_version_19_13

Revision ID: 34b2b6ca345e
Revises: 43995f4ac823

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34b2b6ca345e'
down_revision = '43995f4ac823'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='19.13'))


def downgrade():
    pass
