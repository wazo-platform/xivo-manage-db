"""bump_version_25_01

Revision ID: a2541348bcae
Revises: 710bfcfde4bd

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2541348bcae'
down_revision = '710bfcfde4bd'


def upgrade():
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='25.01'))


def downgrade():
    pass
