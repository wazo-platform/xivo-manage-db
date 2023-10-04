"""revert_bump_version_23_14

Revision ID: 4fad8395b151
Revises: 7c04166bf667

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4fad8395b151'
down_revision = '7c04166bf667'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='23.13'))


def downgrade():
    pass
