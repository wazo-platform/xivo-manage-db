"""bump_version_23_13

Revision ID: 43b515cb6968
Revises: 30705dba3484

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43b515cb6968'
down_revision = '30705dba3484'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='23.13'))


def downgrade():
    pass
