"""bump_version_21_11

Revision ID: 06e9e3483fec
Revises: 907d4947d665

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06e9e3483fec'
down_revision = '907d4947d665'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='21.11'))


def downgrade():
    pass
