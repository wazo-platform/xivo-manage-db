"""bump_version_26_11

Revision ID: c6a2fbdd654a
Revises: fd20c42ff93c

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = 'c6a2fbdd654a'
down_revision = 'fd20c42ff93c'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='26.11'))


def downgrade():
    pass
