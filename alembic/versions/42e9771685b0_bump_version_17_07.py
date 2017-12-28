"""bump_version_17_07

Revision ID: 42e9771685b0
Revises: 596b177ba681

"""

# revision identifiers, used by Alembic.
revision = '42e9771685b0'
down_revision = '596b177ba681'

from alembic import op
import sqlalchemy as sa


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='17.07'))


def downgrade():
    pass
