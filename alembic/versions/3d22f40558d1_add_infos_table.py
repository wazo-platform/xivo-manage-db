"""add infos table

Revision ID: 3d22f40558d1
Revises: 24b41ddb07d7

"""
from alembic import op
import uuid

import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d22f40558d1'
down_revision = '24b41ddb07d7'


def upgrade():
    op.create_table(
        'infos',
        sa.Column('uuid', sa.String(38), nullable=False),
        sa.PrimaryKeyConstraint('uuid')
    )

    xivo_uuid = unicode(uuid.uuid5(uuid.NAMESPACE_DNS, __name__))
    infos_table = sa.sql.table('infos', sa.sql.column('uuid'))
    infos_query = infos_table.insert().values(uuid=xivo_uuid)
    op.get_bind().execute(infos_query)


def downgrade():
    op.drop_table('infos')
