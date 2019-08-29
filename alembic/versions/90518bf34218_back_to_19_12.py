"""back-to-19.12

Revision ID: 90518bf34218
Revises: b3bf380f5241

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90518bf34218'
down_revision = 'b3bf380f5241'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='19.12'))


def downgrade():
    pass
