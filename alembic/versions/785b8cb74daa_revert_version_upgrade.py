"""revert version upgrade

Revision ID: 785b8cb74daa
Revises: 93ea61395eef

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '785b8cb74daa'
down_revision = '93ea61395eef'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='21.16'))


def downgrade():
    pass
