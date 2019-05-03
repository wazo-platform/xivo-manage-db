"""queueskill add tenant_uuid

Revision ID: eaffdf929dd1
Revises: 0aeb61795700

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eaffdf929dd1'
down_revision = '0aeb61795700'

queueskill_tbl = sa.sql.table(
    'queueskill',
    sa.sql.column('id'),
    sa.sql.column('catid'),
    sa.sql.column('tenant_uuid'),
    sa.sql.column('name'),
    sa.sql.column('description'),
)

agentqueueskill_tbl = sa.sql.table(
    'agentqueueskill',
    sa.sql.column('agentid'),
    sa.sql.column('skillid'),
)

agentfeatures_tbl = sa.sql.table(
    'agentfeatures',
    sa.sql.column('id'),
    sa.sql.column('tenant_uuid'),
)


def associate_tenants():
    # 1. Find the agent-skill associations
    query = (
        sa.sql.select([
            agentqueueskill_tbl.c.agentid,
            agentqueueskill_tbl.c.skillid,
            agentfeatures_tbl.c.tenant_uuid,
        ])
        .where(agentfeatures_tbl.c.id == agentqueueskill_tbl.c.agentid)
    )
    agent_skill_associations = op.get_bind().execute(query)

    # 2. Set the agent tenant to the skill
    # skill_migrated = {skill_id: set(tenant_uuids)}
    skill_migrated = dict()
    for agent_id, skill_id, tenant_uuid in agent_skill_associations:
        # New skill id, update the one existing in the db
        if skill_id not in skill_migrated:
            query = (
                queueskill_tbl.update()
                .where(queueskill_tbl.c.id == skill_id)
                .values(tenant_uuid=tenant_uuid)
            )
            op.execute(query)
            skill_migrated[skill_id] = {tenant_uuid}
        else:
            # create a copy of the skill if the tenant is not the same and update the relationship
            # with the new id
            if tenant_uuid not in skill_migrated[skill_id]:
                query = (
                    sa.sql.select([
                        queueskill_tbl.c.catid,
                        queueskill_tbl.c.name,
                        queueskill_tbl.c.description,
                    ])
                    .where(queueskill_tbl.c.id == skill_id)
                )
                result = op.get_bind().execute(query).first()

                query = (
                    queueskill_tbl.insert()
                    .returning(queueskill_tbl.c.id)
                    .values(tenant_uuid=tenant_uuid, **result)
                )
                inserted_id = op.get_bind().execute(query).scalar()

                query = (
                    agentqueueskill_tbl.update()
                    .where(
                        sa.sql.and_(
                            agentqueueskill_tbl.c.agentid == agent_id,
                            agentqueueskill_tbl.c.skillid == skill_id,
                        )
                    )
                    .values(skillid=inserted_id)
                )
                op.execute(query)
                skill_migrated[skill_id].add(tenant_uuid)


def delete_no_tenants():
    query = (
        queueskill_tbl.delete()
        .where(queueskill_tbl.c.tenant_uuid == None)  # noqa
    )
    op.execute(query)


def upgrade():
    op.add_column(
        'queueskill',
        sa.Column(
            'tenant_uuid',
            sa.String(36),
            sa.ForeignKey('tenant.uuid', ondelete='CASCADE'),
            nullable=True
        ),
    )
    op.drop_constraint('queueskill_name_key', 'queueskill', type_='unique')

    op.create_unique_constraint('queueskill_name_tenant_uuid_key', 'queueskill', ['name', 'tenant_uuid'])

    associate_tenants()
    delete_no_tenants()

    op.alter_column('queueskill', 'tenant_uuid', nullable=False)


def downgrade():
    op.drop_column('queueskill', 'tenant_uuid')

    # Find the duplicates and reassociate with the first value, delete the others
    query = (
        sa.sql.select([
            queueskill_tbl.c.id,
            queueskill_tbl.c.name,
        ])
    )
    results = op.get_bind().execute(query)

    skills_unique = dict()
    for skill_id, name in results:
        if name not in skills_unique:
            skills_unique[name] = [skill_id]
        else:
            skills_unique[name].append(skill_id)

    for name, ids in skills_unique.items():
        if len(ids) > 1:
            skill_to_keep = ids[0]
            skills_to_delete = ids[1:]

            for skill_id in skills_to_delete:
                query = (
                    agentqueueskill_tbl.update()
                    .where(
                        agentqueueskill_tbl.c.skillid == skill_id
                    )
                    .values(skillid=skill_to_keep)
                )
                op.execute(query)

                query = (
                    queueskill_tbl.delete()
                    .where(
                        queueskill_tbl.c.id == skill_id
                    )
                )
                op.execute(query)

    op.drop_constraint('queueskill_name_tenant_uuid_key', 'queueskill', type_='unique')
    op.create_unique_constraint('queueskill_name_key', 'queueskill', ['name'])
