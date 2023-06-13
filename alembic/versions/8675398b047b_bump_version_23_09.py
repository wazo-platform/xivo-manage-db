"""bump_version_23_09

Revision ID: 8675398b047b
Revises: b1b59f3b0a5c

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8675398b047b'
down_revision = 'b1b59f3b0a5c'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='23.09'))


def downgrade():
    pass
