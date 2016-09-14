"""remove dialaction n plus 101 option

Revision ID: 544f8b1e6905
Revises: 4977a626c01

"""

# revision identifiers, used by Alembic.
revision = '544f8b1e6905'
down_revision = '4977a626c01'

from alembic import op
from sqlalchemy import sql


dialaction = sql.table('dialaction',
                       sql.column('action'),
                       sql.column('actionarg2'))

schedule = sql.table('schedule',
                     sql.column('fallback_action'),
                     sql.column('fallback_actionargs'))

schedule_time = sql.table('schedule_time',
                          sql.column('action'),
                          sql.column('actionargs'))

ACTIONS = ['sound', 'voicemail']


def upgrade():
    fix_dialactions()
    fix_schedules()


def fix_dialactions():
    op.execute(dialaction.update()
               .where(
                   sql.and_(dialaction.c.action.in_(ACTIONS),
                            dialaction.c.actionarg2 != None))  # noqa
               .values(actionarg2=sql.func.nullif(sql.func.replace(dialaction.c.actionarg2, 'j', ''), '')))


def fix_schedules():
    op.execute(schedule.update()
               .where(
                   sql.and_(schedule.c.fallback_action.in_(ACTIONS),
                            schedule.c.fallback_actionargs != None))  # noqa
               .values(fallback_actionargs=sql.func.replace(schedule.c.fallback_actionargs, 'j;', '')))

    op.execute(schedule_time.update()
               .where(
                   sql.and_(schedule_time.c.action.in_(ACTIONS),
                            schedule_time.c.actionargs != None))  # noqa
               .values(actionargs=sql.func.nullif(sql.func.replace(schedule_time.c.actionargs, 'j;', ''), '')))


def downgrade():
    pass
