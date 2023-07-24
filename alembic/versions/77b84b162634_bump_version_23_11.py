"""bump_version_23_11

Revision ID: 77b84b162634
Revises: b4fb4eb3cf8e

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77b84b162634'
down_revision = 'b4fb4eb3cf8e'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='23.11'))


def downgrade():
    pass
