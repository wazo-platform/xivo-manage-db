"""change dataX columns to type text

Revision ID: 2acff5c02871
Revises: 501dae22d6be

"""

# revision identifiers, used by Alembic.
revision = '2acff5c02871'
down_revision = '501dae22d6be'

from alembic import op
from sqlalchemy.types import Text


def upgrade():
    op.alter_column('queue_log', 'data1', type_=Text)
    op.alter_column('queue_log', 'data2', type_=Text)
    op.alter_column('queue_log', 'data3', type_=Text)
    op.alter_column('queue_log', 'data4', type_=Text)
    op.alter_column('queue_log', 'data5', type_=Text)


def downgrade():
    pass
