"""bump_version_18_04

Revision ID: 1747774cead4
Revises: 28443bfc4fb1

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1747774cead4'
down_revision = '28443bfc4fb1'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='18.04'))


def downgrade():
    pass
