"""bump_version_20_05

Revision ID: 2cbd52dd69e1
Revises: 1c95890bb00d

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2cbd52dd69e1'
down_revision = '1c95890bb00d'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='20.05'))


def downgrade():
    pass
