"""bump_version_21_03

Revision ID: 867bd9268824
Revises: e5281e98b300

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '867bd9268824'
down_revision = 'e5281e98b300'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='21.03'))


def downgrade():
    pass
