"""bump-version-23-11

Revision ID: 1ec7cdef9eeb
Revises: 898154753a9b

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ec7cdef9eeb'
down_revision = '898154753a9b'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='23.11'))


def downgrade():
    pass
