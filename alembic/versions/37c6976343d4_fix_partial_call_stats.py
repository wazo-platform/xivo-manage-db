"""fix_partial_call_stats

Revision ID: 37c6976343d4
Revises: 5073b1fa473e
XiVO Version: <version>

"""

# revision identifiers, used by Alembic.
revision = '37c6976343d4'
down_revision = 'dd011dfbb5'

from alembic import op

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
    op.execute('DROP FUNCTION IF EXISTS "fill_answered_calls"(text, text)')


def downgrade():
    op.execute(old_procedure)
