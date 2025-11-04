"""bump_version_25_16

Revision ID: 040b55af6f67
Revises: 22b03291f3ac

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = '040b55af6f67'
down_revision = '22b03291f3ac'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='25.16'))


def downgrade():
    pass
