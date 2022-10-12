"""bump_version_22_15

Revision ID: 495accfabe9f
Revises: 7d342adb6ae1

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '495accfabe9f'
down_revision = '7d342adb6ae1'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='22.15'))


def downgrade():
    pass
