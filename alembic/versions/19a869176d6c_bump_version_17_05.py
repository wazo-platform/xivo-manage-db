"""bump_version_17_05

Revision ID: 19a869176d6c
Revises: 37b9ac945437

"""

# revision identifiers, used by Alembic.
revision = '19a869176d6c'
down_revision = '37b9ac945437'

from alembic import op
import sqlalchemy as sa


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='17.05'))


def downgrade():
    pass
