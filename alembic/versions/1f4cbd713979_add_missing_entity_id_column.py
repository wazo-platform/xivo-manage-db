"""add_entity_to_callfilter

Revision ID: 1f4cbd713979
Revises: 6bfd932df2c
Create Date: 2014-05-28 14:42:23.479319
XiVO Version: <version>

"""

from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.types import Integer
from sqlalchemy import text

# revision identifiers, used by Alembic.
revision = '1f4cbd713979'
down_revision = '6bfd932df2c'

from alembic import op


def upgrade():
    op.add_column('callfilter',
                  Column('entity_id', Integer, ForeignKey('entity.id'), server_default=text('NULL')))
    op.add_column('pickup',
                  Column('entity_id', Integer, ForeignKey('entity.id'), server_default=text('NULL')))
    op.add_column('schedule',
                  Column('entity_id', Integer, ForeignKey('entity.id'), server_default=text('NULL')))


def downgrade():
    op.drop_column('callfilter', 'entity_id')
    op.drop_column('pickup', 'entity_id')
    op.drop_column('schedule', 'entity_id')
