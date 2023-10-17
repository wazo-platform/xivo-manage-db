"""bump_version_23_15

Revision ID: bcc124448097
Revises: 9ce1ffce9f15

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bcc124448097'
down_revision = '9ce1ffce9f15'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='23.15'))


def downgrade():
    pass
