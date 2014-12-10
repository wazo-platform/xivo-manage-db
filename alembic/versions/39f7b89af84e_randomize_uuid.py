"""randomize uuid

Revision ID: 39f7b89af84e
Revises: 3770e116222d

"""

# revision identifiers, used by Alembic.
revision = '39f7b89af84e'
down_revision = '3770e116222d'

import uuid
from alembic import op
import sqlalchemy as sa


infos_table = sa.sql.table('infos', sa.sql.column('uuid'))


def upgrade():
    new_uuid = unicode(uuid.uuid4())
    infos_query = infos_table.update().values({'uuid': new_uuid})
    op.get_bind().execute(infos_query)


def downgrade():
    pass
