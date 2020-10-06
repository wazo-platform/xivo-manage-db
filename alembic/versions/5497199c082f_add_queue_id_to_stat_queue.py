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


def downgrade():
    rename_column_fk('stat_queue_periodic', 'stat_queue_id', 'queue_id', 'stat_queue')
    rename_column_fk('stat_call_on_queue', 'stat_queue_id', 'queue_id', 'stat_queue')
    rename_column_fk('stat_agent_periodic', 'stat_agent_id', 'agent_id', 'stat_agent')
    rename_column_fk('stat_call_on_queue', 'stat_agent_id', 'agent_id', 'stat_agent')
    op.drop_column('stat_queue', 'queue_id')
    op.drop_column('stat_agent', 'agent_id')
