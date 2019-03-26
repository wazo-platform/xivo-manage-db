"""switchboard_add_tenant_uuid

Revision ID: 12f9880ae872
Revises: 5576b5f933e6

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '12f9880ae872'
down_revision = '5576b5f933e6'


switchboard_tbl = sa.sql.table(
    'switchboard',
    sa.sql.column('uuid'),
    sa.sql.column('tenant_uuid'),
)
switchboard_member_user_tbl = sa.sql.table(
    'switchboard_member_user',
    sa.sql.column('switchboard_uuid'),
    sa.sql.column('user_uuid'),
)
incall_tbl = sa.sql.table(
    'incall',
    sa.sql.column('id'),
    sa.sql.column('tenant_uuid'),
)
dialaction_tbl = sa.sql.table(
    'dialaction',
    sa.sql.column('category'),
    sa.sql.column('categoryval'),
    sa.sql.column('action'),
    sa.sql.column('actionarg1'),
)
userfeatures_tbl = sa.sql.table(
    'userfeatures',
    sa.sql.column('uuid'),
    sa.sql.column('tenant_uuid'),
)


def associate_tenants():

    query = (
        sa.sql.select([switchboard_tbl.c.uuid, incall_tbl.c.tenant_uuid])
        .where(dialaction_tbl.c.category == 'incall')
        .where(dialaction_tbl.c.categoryval == sa.cast(incall_tbl.c.id, sa.String))
        .where(dialaction_tbl.c.action == 'switchboard')
        .where(dialaction_tbl.c.actionarg1 == switchboard_tbl.c.uuid)
    )
    switchboard_incall = op.get_bind().execute(query)

    query = (
        sa.sql.select([switchboard_tbl.c.uuid, userfeatures_tbl.c.tenant_uuid])
        .where(switchboard_member_user_tbl.c.switchboard_uuid == switchboard_tbl.c.uuid)
        .where(switchboard_member_user_tbl.c.user_uuid == userfeatures_tbl.c.uuid)
    )
    switchboard_user = op.get_bind().execute(query)

    for switchboard_uuid, tenant_uuid in list(switchboard_incall) + list(switchboard_user):
        query = (
            switchboard_tbl.update()
            .where(switchboard_tbl.c.uuid == switchboard_uuid)
            .values(tenant_uuid=tenant_uuid)
        )
        op.execute(query)


def delete_user_not_in_same_incall_tenant():
    query = (
        sa.sql.select([switchboard_tbl.c.uuid])
        .where(dialaction_tbl.c.category == 'incall')
        .where(dialaction_tbl.c.categoryval == sa.cast(incall_tbl.c.id, sa.String))
        .where(dialaction_tbl.c.action == 'switchboard')
        .where(dialaction_tbl.c.actionarg1 == switchboard_tbl.c.uuid)
        .where(switchboard_member_user_tbl.c.switchboard_uuid == switchboard_tbl.c.uuid)
        .where(switchboard_member_user_tbl.c.user_uuid == userfeatures_tbl.c.uuid)
        .where(incall_tbl.c.tenant_uuid != userfeatures_tbl.c.tenant_uuid)
    )
    switchboards = op.get_bind().execute(query)

    # Keep tenant from incall and delete user
    for switchboard in switchboards:
        query = (
            switchboard_member_user_tbl.delete()
            .where(switchboard_member_user_tbl.c.switchboard_uuid == switchboard.uuid)
        )
        op.execute(query)


def delete_next_incall_not_in_same_tenant():
    query = (
        sa.sql.select([switchboard_tbl.c.uuid, incall_tbl.c.id, incall_tbl.c.tenant_uuid])
        .where(dialaction_tbl.c.category == 'incall')
        .where(dialaction_tbl.c.categoryval == sa.cast(incall_tbl.c.id, sa.String))
        .where(dialaction_tbl.c.action == 'switchboard')
        .where(dialaction_tbl.c.actionarg1 == switchboard_tbl.c.uuid)
    )
    result = op.get_bind().execute(query)

    # Delete dialaction if there are not in the same tenant
    cache = {}
    for switchboard_uuid, incall_id, tenant_uuid in result:
        cache.setdefault(switchboard_uuid, tenant_uuid)
        if cache[switchboard_uuid] == tenant_uuid:
            continue

        query = (
            dialaction_tbl.delete()
            .where(dialaction_tbl.c.category == 'incall')
            .where(dialaction_tbl.c.categoryval == str(incall_id))
        )
        op.execute(query)


def delete_next_user_not_in_same_tenant():
    query = (
        sa.sql.select([switchboard_tbl.c.uuid, userfeatures_tbl.c.uuid, userfeatures_tbl.c.tenant_uuid])
        .where(switchboard_member_user_tbl.c.switchboard_uuid == switchboard_tbl.c.uuid)
        .where(switchboard_member_user_tbl.c.user_uuid == userfeatures_tbl.c.uuid)
    )
    result = op.get_bind().execute(query)

    # Delete member user if there are not in the same tenant
    cache = {}
    for switchboard_uuid, user_uuid, tenant_uuid in result:
        cache.setdefault(switchboard_uuid, tenant_uuid)
        if cache[switchboard_uuid] == tenant_uuid:
            continue

        query = (
            switchboard_member_user_tbl.delete()
            .where(switchboard_member_user_tbl.c.switchboard_uuid == switchboard_uuid)
            .where(switchboard_member_user_tbl.c.user_uuid == user_uuid)
        )
        op.execute(query)


def delete_no_tenants():
    query = sa.sql.select([switchboard_tbl.c.uuid]).where(switchboard_tbl.c.tenant_uuid == None)  # noqa
    switchboards = op.get_bind().execute(query)
    for (switchboard_uuid,) in switchboards:
        query = (
            switchboard_member_user_tbl.delete()
            .where(switchboard_member_user_tbl.c.switchboard_uuid == switchboard_uuid)
        )
        op.execute(query)
        query = switchboard_tbl.delete().where(switchboard_tbl.c.uuid == switchboard_uuid)
        op.execute(query)


def delete_unhandled_dialaction():
    query = (
        dialaction_tbl.delete()
        .where(dialaction_tbl.c.category != 'incall')
        .where(dialaction_tbl.c.action == 'switchboard')
    )
    op.execute(query)


def upgrade():
    op.add_column(
        'switchboard',
        sa.Column(
            'tenant_uuid',
            sa.String(36),
            sa.ForeignKey('tenant.uuid', ondelete='CASCADE'),
            nullable=True),
    )
    delete_user_not_in_same_incall_tenant()
    delete_next_incall_not_in_same_tenant()
    delete_next_user_not_in_same_tenant()
    associate_tenants()
    delete_unhandled_dialaction()
    delete_no_tenants()
    op.alter_column('switchboard', 'tenant_uuid', nullable=False)


def downgrade():
    op.drop_column('switchboard', 'tenant_uuid')
