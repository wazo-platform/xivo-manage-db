"""bump_version_22_04

Revision ID: 0ffacfab7041
Revises: 5863384621a1

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ffacfab7041'
down_revision = '5863384621a1'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='22.04'))


def downgrade():
    pass
