"""bump_version_26_06

Revision ID: 8863a45bcbd0
Revises: 6e41fc32adcb

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = '8863a45bcbd0'
down_revision = '6e41fc32adcb'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='26.06'))


def downgrade():
    pass
