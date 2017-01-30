"""add moh table

Revision ID: 33fa1a10428f
Revises: 34122e276b2

"""

# revision identifiers, used by Alembic.
revision = '33fa1a10428f'
down_revision = '34122e276b2'

from alembic import op
from sqlalchemy import Column, PrimaryKeyConstraint, String, Text, UniqueConstraint


def upgrade():
    op.create_table(
        'moh',
        Column('uuid', String(38), nullable=False),
        Column('name', Text, nullable=False),
        Column('label', Text),
        Column('mode', Text, nullable=False),
        Column('application', Text),
        Column('sort', Text),
        PrimaryKeyConstraint('uuid'),
        UniqueConstraint('name'),
    )



def downgrade():
    op.drop_table('moh')
