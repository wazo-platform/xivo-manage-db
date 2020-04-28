"""add-greeting-sound-to-incall

Revision ID: 2a27e01c8070
Revises: 4c660492b365

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a27e01c8070'
down_revision = '4c660492b365'

TABLE = 'incall'


def upgrade():
    op.add_column(TABLE, sa.Column('greeting_sound', sa.Text))


def downgrade():
    op.drop_column(TABLE, 'greeting_sound')
