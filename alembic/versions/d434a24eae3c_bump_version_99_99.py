"""bump_version_99_99

Revision ID: d434a24eae3c
Revises: 4c660492b365

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd434a24eae3c'
down_revision = '4c660492b365'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='99.99'))


def downgrade():
    pass
