"""back to 19.13

Revision ID: fbbbf7d78ed0
Revises: 90518bf34218

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbbbf7d78ed0'
down_revision = '90518bf34218'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='19.13'))


def downgrade():
    pass
