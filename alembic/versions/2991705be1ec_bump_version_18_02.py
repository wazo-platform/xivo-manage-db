"""bump_version_18_02

Revision ID: 2991705be1ec
Revises: 18840b2fdb03

"""

# revision identifiers, used by Alembic.
revision = '2991705be1ec'
down_revision = '18840b2fdb03'

from alembic import op
import sqlalchemy as sa


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='18.02'))


def downgrade():
    pass
