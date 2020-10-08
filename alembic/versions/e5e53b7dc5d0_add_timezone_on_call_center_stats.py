"""add-timezone-on-call-center-stats

Revision ID: e5e53b7dc5d0
Revises: 5497199c082f

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'e5e53b7dc5d0'
down_revision = '5497199c082f'


def upgrade():
    op.alter_column('stat_agent_periodic', 'time', type_=sa.DateTime(timezone=True))
    op.alter_column('stat_queue_periodic', 'time', type_=sa.DateTime(timezone=True))
    op.alter_column('stat_call_on_queue', 'time', type_=sa.DateTime(timezone=True))
    op.alter_column('queue_log', 'time', server_default=None, nullable=True)
    op.alter_column(
        'queue_log',
        'time',
        type_=sa.DateTime(timezone=True),
        postgresql_using='"time"::timestamp with time zone',
    )

    op.execute('DROP FUNCTION IF EXISTS "fill_simple_calls" (text, text);')
    op.execute('DROP FUNCTION IF EXISTS "fill_simple_calls" (timestamptz, timestamptz);')
    op.execute("""
CREATE FUNCTION "fill_simple_calls"(period_start timestamptz, period_end timestamptz)
  RETURNS void AS
$$
  INSERT INTO "stat_call_on_queue" (callid, "time", stat_queue_id, status)
    SELECT
      callid,
      time,
      (SELECT id FROM stat_queue WHERE name=queuename) as stat_queue_id,
      CASE WHEN event = 'FULL' THEN 'full'::call_exit_type
           WHEN event = 'DIVERT_CA_RATIO' THEN 'divert_ca_ratio'
           WHEN event = 'DIVERT_HOLDTIME' THEN 'divert_waittime'
           WHEN event = 'CLOSED' THEN 'closed'
           WHEN event = 'JOINEMPTY' THEN 'joinempty'
      END as status
    FROM queue_log
    WHERE event IN ('FULL', 'DIVERT_CA_RATIO', 'DIVERT_HOLDTIME', 'CLOSED', 'JOINEMPTY') AND
          "time" BETWEEN $1 AND $2;
$$
LANGUAGE SQL;
               """)
    op.execute('DROP FUNCTION IF EXISTS "fill_leaveempty_calls" (text, text);')
    op.execute('DROP FUNCTION IF EXISTS "fill_leaveempty_calls" (timestamptz, timestamptz);')
    op.execute("""
CREATE OR REPLACE FUNCTION "fill_leaveempty_calls" (period_start timestamptz, period_end timestamptz)
  RETURNS void AS
$$
INSERT INTO stat_call_on_queue (callid, time, waittime, stat_queue_id, status)
SELECT
  callid,
  enter_time as time,
  EXTRACT(EPOCH FROM (leave_time - enter_time))::INTEGER as waittime,
  stat_queue_id,
  'leaveempty' AS status
FROM (SELECT
        time AS enter_time,
        (select time from queue_log where callid=main.callid AND event='LEAVEEMPTY' LIMIT 1) AS leave_time,
        callid,
        (SELECT id FROM stat_queue WHERE name=queuename) AS stat_queue_id
      FROM queue_log AS main
      WHERE callid IN (SELECT callid FROM queue_log WHERE event = 'LEAVEEMPTY')
            AND event = 'ENTERQUEUE'
            AND time BETWEEN $1 AND $2) AS first;
$$
LANGUAGE SQL;
               """)
    # NOTE(fblackburn): fix column to match asterisk recommends
    op.alter_column(
        'queue_log',
        'callid',
        type_=sa.String(80),
        server_default=None,
        nullable=True,
    )
    op.alter_column(
        'queue_log',
        'queuename',
        type_=sa.String(256),
        server_default=None,
        nullable=True
    )
    op.alter_column('queue_log', 'agent', server_default=None, nullable=True)
    op.alter_column('queue_log', 'event', server_default=None, nullable=True)
    op.alter_column('queue_log', 'data1', server_default=None)
    op.alter_column('queue_log', 'data2', server_default=None)
    op.alter_column('queue_log', 'data3', server_default=None)
    op.alter_column('queue_log', 'data4', server_default=None)
    op.alter_column('queue_log', 'data5', server_default=None)


def downgrade():
    op.alter_column('queue_log', 'data5', server_default='')
    op.alter_column('queue_log', 'data4', server_default='')
    op.alter_column('queue_log', 'data3', server_default='')
    op.alter_column('queue_log', 'data2', server_default='')
    op.alter_column('queue_log', 'data1', server_default='')
    op.alter_column('queue_log', 'event', server_default='', nullable=False)
    op.alter_column('queue_log', 'agent', server_default='', nullable=False)
    op.alter_column(
        'queue_log',
        'queuename',
        type_=sa.String(50),
        server_default='',
        nullable=False,
    )
    op.alter_column(
        'queue_log',
        'callid',
        type_=sa.String(32),
        server_default='',
        nullable=False,
    )
    op.alter_column('queue_log', 'time', type_=sa.String(80))
    op.alter_column('queue_log', 'time', server_default='', nullable=False)
    op.alter_column('stat_call_on_queue', 'time', type_=sa.DateTime())
    op.alter_column('stat_queue_periodic', 'time', type_=sa.DateTime())
    op.alter_column('stat_agent_periodic', 'time', type_=sa.DateTime())
