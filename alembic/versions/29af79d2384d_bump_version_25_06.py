"""bump_version_25_06

Revision ID: 29af79d2384d
Revises: 1cbfa6e85796

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = '29af79d2384d'
down_revision = '1cbfa6e85796'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='25.06'))


def downgrade():
    pass
