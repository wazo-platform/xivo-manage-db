"""bump_version_26_03

Revision ID: e01c44b679ed
Revises: 85fdd3fb9cde

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = 'e01c44b679ed'
down_revision = '85fdd3fb9cde'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='26.03'))


def downgrade():
    pass
