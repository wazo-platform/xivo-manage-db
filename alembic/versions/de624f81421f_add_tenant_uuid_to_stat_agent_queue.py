"""add tenant uuid to stat-agent/queue

Revision ID: de624f81421f
Revises: b78a74e69592

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de624f81421f'
down_revision = 'b78a74e69592'

stat_queue_table = sa.sql.table(
    'stat_queue',
    sa.sql.column('id'),
    sa.sql.column('name'),
    sa.sql.column('tenant_uuid'),
)
stat_call_on_queue_table = sa.sql.table(
    'stat_call_on_queue',
    sa.sql.column('queue_id'),
    sa.sql.column('agent_id'),
)
stat_queue_periodic_table = sa.sql.table(
    'stat_queue_periodic',
    sa.sql.column('queue_id'),
)
queuefeatures_table = sa.sql.table(
    'queuefeatures',
    sa.sql.column('id'),
    sa.sql.column('name'),
    sa.sql.column('tenant_uuid'),
)

stat_agent_table = sa.sql.table(
    'stat_agent',
    sa.sql.column('id'),
    sa.sql.column('name'),
    sa.sql.column('tenant_uuid'),
)
stat_agent_periodic_table = sa.sql.table(
    'stat_agent_periodic',
    sa.sql.column('agent_id'),
)
agentfeatures_table = sa.sql.table(
    'agentfeatures',
    sa.sql.column('id'),
    sa.sql.column('number'),
    sa.sql.column('tenant_uuid'),
)


def _add_tenant_to_queues():
    query = (
        stat_queue_table
        .update()
        .values(tenant_uuid=queuefeatures_table.c.tenant_uuid)
        .where(stat_queue_table.c.name == queuefeatures_table.c.name)
    )
    op.execute(query)


def _delete_queues_without_tenant():
    deleted_queue_ids_query = (
        sa.sql.select([stat_queue_table.c.id])
        .where(stat_queue_table.c.tenant_uuid == None)
    )
    delete_query = (
        stat_call_on_queue_table
        .delete()
        .where(stat_call_on_queue_table.c.queue_id.in_(deleted_queue_ids_query))
    )
    op.execute(delete_query)
    delete_query = (
        stat_queue_periodic_table
        .delete()
        .where(stat_queue_periodic_table.c.queue_id.in_(deleted_queue_ids_query))
    )
    op.execute(delete_query)
    delete_query = (
        stat_queue_table
        .delete()
        .where(stat_queue_table.c.id.in_(deleted_queue_ids_query))
    )
    op.execute(delete_query)


def _add_tenant_to_agents():
    query = (
        stat_agent_table
        .update()
        .values(tenant_uuid=agentfeatures_table.c.tenant_uuid)
        .where(stat_agent_table.c.name == sa.func.concat('Agent/', agentfeatures_table.c.number))
    )
    op.execute(query)


def _delete_agents_without_tenant():
    deleted_agent_ids_query = (
        sa.sql.select([stat_agent_table.c.id])
        .where(stat_agent_table.c.tenant_uuid == None)
    )
    delete_query = (
        stat_call_on_queue_table
        .delete()
        .where(stat_call_on_queue_table.c.agent_id.in_(deleted_agent_ids_query))
    )
    op.execute(delete_query)
    delete_query = (
        stat_agent_periodic_table
        .delete()
        .where(stat_agent_periodic_table.c.agent_id.in_(deleted_agent_ids_query))
    )
    op.execute(delete_query)
    delete_query = (
        stat_agent_table
        .delete()
        .where(stat_agent_table.c.id.in_(deleted_agent_ids_query))
    )
    op.execute(delete_query)


def upgrade():
    op.add_column(
        'stat_queue',
        sa.Column(
            'tenant_uuid',
            sa.String(36),
            nullable=True),
    )
    _add_tenant_to_queues()
    _delete_queues_without_tenant()
    op.alter_column('stat_queue', 'tenant_uuid', nullable=False)

    op.add_column(
        'stat_agent',
        sa.Column(
            'tenant_uuid',
            sa.String(36),
            nullable=True),
    )
    _add_tenant_to_agents()
    _delete_agents_without_tenant()
    op.alter_column('stat_agent', 'tenant_uuid', nullable=False)


def downgrade():
    op.drop_column('stat_queue', 'tenant_uuid')
    op.drop_column('stat_agent', 'tenant_uuid')
