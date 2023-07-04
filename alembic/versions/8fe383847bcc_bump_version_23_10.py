"""bump_version_23_10

Revision ID: 8fe383847bcc
Revises: 8675398b047b

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fe383847bcc'
down_revision = '8675398b047b'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='23.10'))


def downgrade():
    pass
