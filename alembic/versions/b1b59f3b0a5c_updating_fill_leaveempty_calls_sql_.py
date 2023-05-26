"""updating fill_leaveempty_calls sql function to fix misreporting

Revision ID: b1b59f3b0a5c
Revises: e507e100aa92

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1b59f3b0a5c'
down_revision = 'df6812f66958'


old_fill_leaveempty_calls_fn = """
DROP FUNCTION IF EXISTS "fill_leaveempty_calls" (timestamptz, timestamptz);
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
ALTER FUNCTION "fill_leaveempty_calls" (period_start timestamptz, period_end timestamptz) OWNER TO asterisk;
"""

new_fill_leaveempty_calls_fn = """
DROP FUNCTION IF EXISTS "fill_leaveempty_calls" (timestamptz, timestamptz);
CREATE OR REPLACE FUNCTION "fill_leaveempty_calls" (period_start timestamptz, period_end timestamptz)
RETURNS void AS
$$
WITH 
leave_call as (
    SELECT main.id, main.callid, main.time AS leave_time, main.queuename, 
        (SELECT time FROM queue_log 
        WHERE callid = main.callid AND queuename = main.queuename 
        AND time <= main.time AND event = 'ENTERQUEUE' 
        ORDER BY time DESC LIMIT 1) AS enter_time, 
        stat_queue.id as stat_queue_id 
    FROM queue_log AS main 
    LEFT JOIN stat_queue ON stat_queue.name = main.queuename
    WHERE event='LEAVEEMPTY'
),
leave_call_in_range AS (
    SELECT *
    FROM leave_call
    WHERE enter_time BETWEEN $1 AND $2 
)
INSERT INTO stat_call_on_queue (callid, time, waittime, stat_queue_id, status)
SELECT
    callid,
    enter_time AS time,
    EXTRACT(EPOCH FROM (leave_time - enter_time))::INTEGER AS waittime,
    stat_queue_id,
    'leaveempty' AS status
FROM leave_call_in_range;
$$
LANGUAGE SQL;
ALTER FUNCTION "fill_leaveempty_calls" (period_start timestamptz, period_end timestamptz) OWNER TO asterisk;
"""

def upgrade():
    op.get_bind().execute(new_fill_leaveempty_calls_fn)


def downgrade():
    op.get_bind().execute(old_fill_leaveempty_calls_fn)


