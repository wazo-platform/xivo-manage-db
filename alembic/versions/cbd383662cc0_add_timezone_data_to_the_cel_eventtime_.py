"""add timezone data to the cel.eventtime column

Revision ID: cbd383662cc0
Revises: fbbbf7d78ed0

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbd383662cc0'
down_revision = 'fbbbf7d78ed0'


def upgrade():
    op.alter_column('cel', 'eventtime', nullable=False, type_=sa.DateTime(timezone=True))
    op.alter_column('call_log', 'date', type_=sa.DateTime(timezone=True))
    op.alter_column('call_log', 'date_answer', type_=sa.DateTime(timezone=True))
    op.alter_column('call_log', 'date_end', type_=sa.DateTime(timezone=True))


def downgrade():
    op.alter_column('call_log', 'date', type_=sa.DateTime())
    op.alter_column('call_log', 'date_answer', type_=sa.DateTime())
    op.alter_column('call_log', 'date_end', type_=sa.DateTime())
    op.alter_column('cel', 'eventtime', nullable=False, type_=sa.DateTime())
