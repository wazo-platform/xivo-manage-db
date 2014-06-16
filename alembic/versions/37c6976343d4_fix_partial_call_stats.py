"""fix_partial_call_stats

Revision ID: 37c6976343d4
Revises: 5073b1fa473e
Create Date: 2014-06-12 14:32:07.111335
XiVO Version: <version>

"""

# revision identifiers, used by Alembic.
revision = '37c6976343d4'
down_revision = 'dd011dfbb5'

from alembic import op
import sqlalchemy as sa

new_procedure = """
CREATE OR REPLACE FUNCTION "fill_answered_calls"(period_start text, period_end text)
    RETURNS void AS
$$
    INSERT INTO stat_call_on_queue (callid, "time", talktime, waittime, queue_id, agent_id, status)
    (
        WITH
        call_entries AS (
            SELECT
                callid, queuename, agent, time, event, data1, data2, data3, data4
            FROM
                queue_log
            WHERE
                time BETWEEN $1 AND $2
        ),
        call_start AS (
            SELECT
                callid, queuename, time
            FROM
                call_entries
            WHERE
                event = 'ENTERQUEUE'
        ),
        call_end AS (
            SELECT
                callid, queuename, agent, time,
                CASE
                    WHEN event IN ('COMPLETEAGENT', 'COMPLETECALLER')
                        THEN CAST (data2 AS INTEGER)
                    WHEN event = 'TRANSFER'
                        THEN CAST (data4 AS INTEGER)
                END as talktime,
                CASE
                    WHEN event IN ('COMPLETEAGENT', 'COMPLETECALLER')
                        THEN CAST (data1 AS INTEGER)
                    WHEN event = 'TRANSFER'
                        THEN CAST (data3 AS INTEGER)
                END as waittime
            FROM
                call_entries
            WHERE
                event IN ('COMPLETEAGENT', 'COMPLETECALLER', 'TRANSFER')
        ),
        completed_calls AS (
            SELECT
                call_end.callid,
                call_end.queuename,
                call_end.agent,
                call_start.time::TIMESTAMP,
                call_end.talktime,
                call_end.waittime
            FROM
                call_end
                INNER JOIN call_start
                    ON call_end.callid = call_start.callid
                    AND call_end.queuename = call_start.queuename
        ),
        partial_calls AS (
            SELECT
                call_end.callid,
                call_end.queuename,
                call_end.agent,
                call_end.time::TIMESTAMP
                    - (call_end.talktime || ' seconds')::INTERVAL
                    - (call_end.waittime || ' seconds')::INTERVAL
                AS time,
                call_end.talktime,
                call_end.waittime
            FROM
                call_end
                LEFT OUTER JOIN call_start
                    ON call_end.callid = call_start.callid
                    AND call_end.queuename = call_start.queuename
            WHERE
                call_start.callid IS NULL
        ),
        all_calls AS (
            SELECT * FROM completed_calls
            UNION
            SELECT * FROM partial_calls
        )

        SELECT
            all_calls.callid,
            all_calls.time,
            all_calls.talktime,
            all_calls.waittime,
            stat_queue.id as queue_id,
            stat_agent.id as agent_id,
            'answered' AS status
        FROM
            all_calls
        LEFT JOIN
            stat_agent ON all_calls.agent = stat_agent.name
        LEFT JOIN
            stat_queue ON all_calls.queuename = stat_queue.name
        ORDER BY
            all_calls.time
    )
$$
LANGUAGE SQL;
"""

old_procedure = """
CREATE OR REPLACE FUNCTION "fill_answered_calls"(period_start text, period_end text)
  RETURNS void AS
$$
  INSERT INTO stat_call_on_queue (callid, "time", talktime, waittime, queue_id, agent_id, status)
  SELECT
    outer_queue_log.callid,
    CAST ((SELECT "time"
           FROM queue_log
           WHERE callid=outer_queue_log.callid AND
                 queuename=outer_queue_log.queuename AND
                 event='ENTERQUEUE' ORDER BY "time" DESC LIMIT 1) AS TIMESTAMP) AS "time",
    CASE WHEN event IN ('COMPLETEAGENT', 'COMPLETECALLER') THEN CAST (data2 AS INTEGER)
         WHEN event = 'TRANSFER' THEN CAST (data4 AS INTEGER) END as talktime,
    CASE WHEN event IN ('COMPLETEAGENT', 'COMPLETECALLER') THEN CAST (data1 AS INTEGER)
         WHEN event = 'TRANSFER' THEN CAST (data3 AS INTEGER) END as waittime,
    stat_queue.id AS queue_id,
    stat_agent.id AS agent_id,
    'answered' AS status
  FROM
    queue_log as outer_queue_log
  LEFT JOIN
    stat_agent ON outer_queue_log.agent = stat_agent.name
  LEFT JOIN
    stat_queue ON outer_queue_log.queuename = stat_queue.name
  WHERE
    callid IN
      (SELECT callid
       FROM queue_log
       WHERE event = 'ENTERQUEUE' AND "time" BETWEEN $1 AND $2)
    AND event IN ('COMPLETEAGENT', 'COMPLETECALLER', 'TRANSFER');
$$
LANGUAGE SQL;
"""

def upgrade():
    op.execute(new_procedure)


def downgrade():
    op.execute(old_procedure)
