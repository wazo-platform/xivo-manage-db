"""bump_version_18_13

Revision ID: 99082b9c0b7b
Revises: 2256e488e43c

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99082b9c0b7b'
down_revision = '2256e488e43c'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='18.13'))


def downgrade():
    pass
