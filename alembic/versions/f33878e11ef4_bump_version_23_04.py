"""bump_version_23_04

Revision ID: f33878e11ef4
Revises: 9f11f3abaacc

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f33878e11ef4'
down_revision = '9f11f3abaacc'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='23.04'))


def downgrade():
    pass
