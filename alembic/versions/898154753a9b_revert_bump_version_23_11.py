"""revert-bump-version-23-11

Revision ID: 898154753a9b
Revises: 74818b4464a1

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '898154753a9b'
down_revision = '74818b4464a1'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='23.10'))


def downgrade():
    pass
