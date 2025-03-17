"""bump_version_25_05

Revision ID: 1cbfa6e85796
Revises: ba4c449afc9a

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = '1cbfa6e85796'
down_revision = 'ba4c449afc9a'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='25.05'))


def downgrade():
    pass
