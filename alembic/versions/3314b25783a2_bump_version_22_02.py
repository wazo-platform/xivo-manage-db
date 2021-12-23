"""bump_version_22_02

Revision ID: 3314b25783a2
Revises: 0dd3509ac1e2

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3314b25783a2'
down_revision = '0dd3509ac1e2'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='22.02'))


def downgrade():
    pass
