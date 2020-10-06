"""add-queue-id-to-stat-queue

Revision ID: 5497199c082f
Revises: de624f81421f

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5497199c082f'
down_revision = 'de624f81421f'


stat_queue_table = sa.sql.table(
    'stat_queue',
    sa.sql.column('id'),
    sa.sql.column('name'),
    sa.sql.column('queue_id'),
)
queuefeatures_table = sa.sql.table(
    'queuefeatures',
    sa.sql.column('id'),
    sa.sql.column('name'),
)

stat_agent_table = sa.sql.table(
    'stat_agent',
    sa.sql.column('id'),
    sa.sql.column('name'),
    sa.sql.column('agent_id'),
)
agentfeatures_table = sa.sql.table(
    'agentfeatures',
    sa.sql.column('id'),
    sa.sql.column('number'),
)


def _add_queue_id_to_queues():
    query = (
        stat_queue_table
        .update()
        .values(queue_id=queuefeatures_table.c.id)
        .where(stat_queue_table.c.name == queuefeatures_table.c.name)
    )
    op.execute(query)


def _add_agent_id_to_agents():
    query = (
        stat_agent_table
        .update()
        .values(agent_id=agentfeatures_table.c.id)
        .where(stat_agent_table.c.name == sa.func.concat('Agent/', agentfeatures_table.c.number))
    )
    op.execute(query)


def rename_column_fk(table, old_name, new_name, ref_table):
    old_fk_name = f'{table}_{old_name}_fkey'
    new_fk_name = f'{table}_{new_name}_fkey'
    op.alter_column(table, old_name, new_column_name=new_name)
    op.drop_constraint(
        constraint_name=old_fk_name,
        table_name=table,
        type_='foreignkey',
    )
    op.create_foreign_key(
        constraint_name=new_fk_name,
        source_table=table,
        referent_table=ref_table,
        local_cols=[new_name],
        remote_cols=['id'],
    )


def upgrade():
    op.add_column(
        'stat_queue',
        sa.Column(
            'queue_id',
            sa.Integer,
            nullable=True),
    )
    _add_queue_id_to_queues()

    op.add_column(
        'stat_agent',
        sa.Column(
            'agent_id',
            sa.Integer,
            nullable=True),
    )
    _add_agent_id_to_agents()
    rename_column_fk('stat_queue_periodic', 'queue_id', 'stat_queue_id', 'stat_queue')
    rename_column_fk('stat_call_on_queue', 'queue_id', 'stat_queue_id', 'stat_queue')
    rename_column_fk('stat_agent_periodic', 'agent_id', 'stat_agent_id', 'stat_agent')
    rename_column_fk('stat_call_on_queue', 'agent_id', 'stat_agent_id', 'stat_agent')
    op.execute('DROP FUNCTION IF EXISTS "fill_simple_calls" (text, text);')
    op.execute("""
CREATE FUNCTION "fill_simple_calls"(period_start text, period_end text)
  RETURNS void AS
$$
  INSERT INTO "stat_call_on_queue" (callid, "time", stat_queue_id, status)
    SELECT
      callid,
      CAST ("time" AS TIMESTAMP) as "time",
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
    op.execute("""
CREATE OR REPLACE FUNCTION "fill_leaveempty_calls" (period_start text, period_end text)
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
        CAST (time AS TIMESTAMP) AS enter_time,
        (select CAST (time AS TIMESTAMP) from queue_log where callid=main.callid AND event='LEAVEEMPTY' LIMIT 1) AS leave_time,
        callid,
        (SELECT id FROM stat_queue WHERE name=queuename) AS stat_queue_id
      FROM queue_log AS main
      WHERE callid IN (SELECT callid FROM queue_log WHERE event = 'LEAVEEMPTY')
            AND event = 'ENTERQUEUE'
            AND time BETWEEN $1 AND $2) AS first;
$$
LANGUAGE SQL;
               """)


def downgrade():
    rename_column_fk('stat_queue_periodic', 'stat_queue_id', 'queue_id', 'stat_queue')
    rename_column_fk('stat_call_on_queue', 'stat_queue_id', 'queue_id', 'stat_queue')
    rename_column_fk('stat_agent_periodic', 'stat_agent_id', 'agent_id', 'stat_agent')
    rename_column_fk('stat_call_on_queue', 'stat_agent_id', 'agent_id', 'stat_agent')
    op.drop_column('stat_queue', 'queue_id')
    op.drop_column('stat_agent', 'agent_id')
