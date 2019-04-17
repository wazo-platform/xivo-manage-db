"""add tenant_uuid to agentfeatures

Revision ID: 9b0892a818e6
Revises: 560bfca6cf85

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b0892a818e6'
down_revision = '560bfca6cf85'


agentfeatures_tbl = sa.sql.table(
    'agentfeatures',
    sa.sql.column('id'),
    sa.sql.column('tenant_uuid'),
    sa.sql.column('context'),
)

context_tbl = sa.sql.table(
    'context',
    sa.sql.column('name'),
    sa.sql.column('tenant_uuid')
)

agent_login_status_tbl = sa.sql.table(
    'agent_login_status',
    sa.sql.column('agent_id'),
    sa.sql.column('context'),
)
queuefeatures_tbl = sa.sql.table(
    'queuefeatures',
    sa.sql.column('id'),
    sa.sql.column('tenant_uuid'),
    sa.sql.column('name'),
)

queuemember_tbl = sa.sql.table(
    'queuemember',
    sa.sql.column('queue_name'),
    sa.sql.column('interface'),
    sa.sql.column('usertype'),
    sa.sql.column('userid')
)


def associate_tenants():
    query = (
        sa.sql.select([agentfeatures_tbl.c.id, context_tbl.c.tenant_uuid])
        .where(context_tbl.c.name == agentfeatures_tbl.c.context)
    )
    context_agent_tenants = op.get_bind().execute(query)

    query = (
        sa.sql.select([agent_login_status_tbl.c.agent_id, context_tbl.c.tenant_uuid])
        .where(context_tbl.c.name == agent_login_status_tbl.c.context)
    )
    context_login_tenants = op.get_bind().execute(query)

    query = (
        sa.sql.select([queuemember_tbl.c.userid, queuefeatures_tbl.c.tenant_uuid])
        .where(
            sa.sql.and_(
                queuemember_tbl.c.queue_name == queuefeatures_tbl.c.name,
                queuemember_tbl.c.usertype == 'agent',
            )
        )
    )
    queuemember_tenants = op.get_bind().execute(query)

    tenant_sources = (
        list(context_agent_tenants) + list(queuemember_tenants) + list(context_login_tenants)
    )

    already_migrated = []
    for agent_id, tenant_uuid in tenant_sources:
        if agent_id not in already_migrated:
            query = (
                agentfeatures_tbl.update()
                .where(agentfeatures_tbl.c.id == agent_id)
                .values(tenant_uuid=tenant_uuid)
            )
            op.execute(query)
            already_migrated.append(agent_id)


def delete_no_tenants():
    query = (
        agentfeatures_tbl.delete()
        .where(agentfeatures_tbl.c.tenant_uuid == None)  # noqa
    )
    op.execute(query)


def upgrade():
    op.add_column(
        'agentfeatures',
        sa.Column(
            'tenant_uuid',
            sa.String(36),
            sa.ForeignKey('tenant.uuid', ondelete='CASCADE'),
            nullable=True
        ),
    )

    associate_tenants()
    delete_no_tenants()

    op.alter_column('agentfeatures', 'tenant_uuid', nullable=False)


def downgrade():
    op.drop_column('agentfeatures', 'tenant_uuid')
