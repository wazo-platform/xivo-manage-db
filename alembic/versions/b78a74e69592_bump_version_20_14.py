"""bump_version_20_14

Revision ID: b78a74e69592
Revises: 040b69fd8297

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b78a74e69592'
down_revision = '040b69fd8297'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='20.14'))


def downgrade():
    pass
