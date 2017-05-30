"""remove_duration_and_answered_from_call_log

Revision ID: 29a5eab6a19b
Revises: 64c6bde0116c

"""

# revision identifiers, used by Alembic.
revision = '29a5eab6a19b'
down_revision = '64c6bde0116c'

from alembic import op
import sqlalchemy as sa


call_log = sa.sql.table('call_log',
                        sa.sql.column('answered'),
                        sa.sql.column('date'),
                        sa.sql.column('date_answer'),
                        sa.sql.column('date_end'),
                        sa.sql.column('duration'))


def upgrade():
    op.execute(call_log.update()
               .where(call_log.c.date_answer == None)
               .where(call_log.c.answered == True)
               .values(date_answer=call_log.c.date))
    op.execute(call_log.update()
               .where(call_log.c.date_end == None)
               .values(date_end=call_log.c.date+call_log.c.duration))
    op.drop_column('call_log', 'answered')
    op.drop_column('call_log', 'duration')


def downgrade():
    pass
