"""add_date_answer_to_call_log

Revision ID: dba4e40979ae
Revises: 3612e8058d92

"""

# revision identifiers, used by Alembic.
revision = 'dba4e40979ae'
down_revision = '3612e8058d92'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('call_log', sa.Column('date_answer', sa.DateTime))


def downgrade():
    op.drop_column('call_log', 'date_answer')
