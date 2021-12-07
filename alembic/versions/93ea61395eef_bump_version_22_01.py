"""bump_version_22_01

Revision ID: 93ea61395eef
Revises: 29290c38946f

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93ea61395eef'
down_revision = '29290c38946f'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='22.01'))


def downgrade():
    pass
