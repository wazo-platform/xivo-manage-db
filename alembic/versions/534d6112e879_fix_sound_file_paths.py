"""fix_sound_file_paths

Revision ID: 534d6112e879
Revises: 35a7f7e2dc33

"""

# revision identifiers, used by Alembic.
from alembic import op
from sqlalchemy import sql

revision = '534d6112e879'
down_revision = '35a7f7e2dc33'


schedule = sql.table('schedule',
                     sql.column('fallback_action'),
                     sql.column('fallback_actionid'))

schedule_time = sql.table('schedule_time',
                          sql.column('action'),
                          sql.column('actionid'))

dialaction = sql.table('dialaction',
                       sql.column('action'),
                       sql.column('actionarg1'))


def upgrade():
    fix_queues()
    fix_schedules()
    fix_dialactions()


def fix_queues():
    query = """
    UPDATE
        queue
    SET
        "announce" = replace("announce", 'pf-xivo', 'xivo'),
        "periodic-announce" = replace("periodic-announce", 'pf-xivo', 'xivo'),
        "queue-youarenext" = replace("queue-youarenext", 'pf-xivo', 'xivo'),
        "queue-thereare" = replace("queue-thereare", 'pf-xivo', 'xivo'),
        "queue-callswaiting" = replace("queue-callswaiting", 'pf-xivo', 'xivo'),
        "queue-holdtime" = replace("queue-holdtime", 'pf-xivo', 'xivo'),
        "queue-minutes" = replace("queue-minutes", 'pf-xivo', 'xivo'),
        "queue-seconds" = replace("queue-seconds", 'pf-xivo', 'xivo'),
        "queue-thankyou" = replace("queue-thankyou", 'pf-xivo', 'xivo'),
        "queue-reporthold" = replace("queue-reporthold", 'pf-xivo', 'xivo')
    WHERE
        announce LIKE '%pf-xivo%'
        OR "periodic-announce" LIKE '%pf-xivo%'
        OR "queue-youarenext" LIKE '%pf-xivo%'
        OR "queue-thereare" LIKE '%pf-xivo%'
        OR "queue-callswaiting" LIKE '%pf-xivo%'
        OR "queue-holdtime" LIKE '%pf-xivo%'
        OR "queue-minutes" LIKE '%pf-xivo%'
        OR "queue-seconds" LIKE '%pf-xivo%'
        OR "queue-thankyou" LIKE '%pf-xivo%'
        OR "queue-reporthold" LIKE '%pf-xivo%'
    """

    op.execute(query)


def fix_schedules():
    schedule_query = (schedule.update()
                      .where(
                          sql.and_(schedule.c.fallback_action == 'sound',
                                   schedule.c.fallback_actionid.like('%pf-xivo%')))
                      .values(fallback_actionid=sql.func.replace(schedule.c.fallback_actionid,
                                                                 'pf-xivo',
                                                                 'xivo')))

    schedule_time_query = (schedule_time.update()
                           .where(
                               sql.and_(schedule_time.c.action == 'sound',
                                        schedule_time.c.actionid.like('%pf-xivo%')))
                           .values(actionid=sql.func.replace(schedule_time.c.actionid,
                                                             'pf-xivo',
                                                             'xivo')))

    op.execute(schedule_query)
    op.execute(schedule_time_query)


def fix_dialactions():
    query = (dialaction.update()
             .where(
                 sql.and_(dialaction.c.action == 'sound',
                          dialaction.c.actionarg1.like('%pf-xivo%')))
             .values(actionarg1=sql.func.replace(dialaction.c.actionarg1,
                                                 'pf-xivo',
                                                 'xivo')))

    op.execute(query)


def downgrade():
    unfix_queues()
    unfix_schedules()
    unfix_dialactions()


def unfix_queues():
    query = """
    UPDATE
        queue
    SET
        "announce" = replace("announce", '/xivo/', '/pf-xivo/'),
        "periodic-announce" = replace("periodic-announce", '/xivo/', '/pf-xivo/'),
        "queue-youarenext" = replace("queue-youarenext", '/xivo/', '/pf-xivo/'),
        "queue-thereare" = replace("queue-thereare", '/xivo/', '/pf-xivo/'),
        "queue-callswaiting" = replace("queue-callswaiting", '/xivo/', '/pf-xivo/'),
        "queue-holdtime" = replace("queue-holdtime", '/xivo/', '/pf-xivo/'),
        "queue-minutes" = replace("queue-minutes", '/xivo/', '/pf-xivo/'),
        "queue-seconds" = replace("queue-seconds", '/xivo/', '/pf-xivo/'),
        "queue-thankyou" = replace("queue-thankyou", '/xivo/', '/pf-xivo/'),
        "queue-reporthold" = replace("queue-reporthold", '/xivo/', '/pf-xivo/')
    WHERE
        "announce" LIKE '%/xivo/%'
        OR "periodic-announce" LIKE '%/xivo/%'
        OR "queue-youarenext" LIKE '%/xivo/%'
        OR "queue-thereare" LIKE '%/xivo/%'
        OR "queue-callswaiting" LIKE '%/xivo/%'
        OR "queue-holdtime" LIKE '%/xivo/%'
        OR "queue-minutes" LIKE '%/xivo/%'
        OR "queue-seconds" LIKE '%/xivo/%'
        OR "queue-thankyou" LIKE '%/xivo/%'
        OR "queue-reporthold" LIKE '%/xivo/%'
    """

    op.execute(query)


def unfix_schedules():
    schedule_query = (schedule.update()
                      .where(
                          sql.and_(schedule.c.fallback_action == 'sound',
                                   schedule.c.fallback_actionid.like('%/xivo/%')))
                      .values(fallback_actionid=sql.func.replace(schedule.c.fallback_actionid,
                                                                 '/xivo/',
                                                                 '/pf-xivo/')))

    schedule_time_query = (schedule_time.update()
                           .where(
                               sql.and_(schedule_time.c.action == 'sound',
                                        schedule_time.c.actionid.like('%/xivo/%')))
                           .values(actionid=sql.func.replace(schedule_time.c.actionid,
                                                             '/xivo/',
                                                             '/pf-xivo/')))

    op.execute(schedule_query)
    op.execute(schedule_time_query)


def unfix_dialactions():
    query = (dialaction.update()
             .where(
                 sql.and_(dialaction.c.action == 'sound',
                          dialaction.c.actionarg1.like('%/xivo/%')))
             .values(actionarg1=sql.func.replace(dialaction.c.actionarg1,
                                                 '/xivo/',
                                                 '/pf-xivo/')))

    op.execute(query)
