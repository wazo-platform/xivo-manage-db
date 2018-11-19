"""bump_version_18_14

Revision ID: 46dda7d0374e
Revises: 99082b9c0b7b

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46dda7d0374e'
down_revision = '99082b9c0b7b'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='18.14'))


def downgrade():
    pass
