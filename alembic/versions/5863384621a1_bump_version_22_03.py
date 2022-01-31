"""bump_version_22_03

Revision ID: 5863384621a1
Revises: 3314b25783a2

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5863384621a1'
down_revision = '3314b25783a2'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='22.03'))


def downgrade():
    pass
