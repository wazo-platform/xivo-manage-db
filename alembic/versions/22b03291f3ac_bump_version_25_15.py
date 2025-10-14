"""bump_version_25_15

Revision ID: 22b03291f3ac
Revises: a997646ba84e

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = '22b03291f3ac'
down_revision = 'a997646ba84e'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='25.15'))


def downgrade():
    pass
