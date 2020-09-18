"""fix-global-trunk-template

Revision ID: 69c55f395eb7
Revises: da53b63d9433

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69c55f395eb7'
down_revision = 'da53b63d9433'

tenant_tbl = sa.sql.table(
    'tenant',
    sa.sql.column('uuid'),
    sa.sql.column('global_trunk_sip_template_uuid'),
    sa.sql.column('global_sip_template_uuid'),
    sa.sql.column('sip_templates_generated'),
)
endpoint_sip_tbl = sa.sql.table(
    'endpoint_sip',
    sa.sql.column('uuid'),
    sa.sql.column('label'),
    sa.sql.column('tenant_uuid'),
)
endpoint_sip_section_tbl = sa.sql.table(
    'endpoint_sip_section',
    sa.sql.column('uuid'),
    sa.sql.column('type'),
    sa.sql.column('endpoint_sip_uuid'),
)
endpoint_sip_section_option_tbl = sa.sql.table(
    'endpoint_sip_section_option',
    sa.sql.column('uuid'),
    sa.sql.column('key'),
    sa.sql.column('value'),
    sa.sql.column('endpoint_sip_section_uuid'),
)
endpoint_sip_template_tbl = sa.sql.table(
    'endpoint_sip_template',
    sa.sql.column('child_uuid'),
    sa.sql.column('parent_uuid'),
)


def find_global_trunk_template_uuid():
    query = sa.sql.select(
        [tenant_tbl.c.global_trunk_sip_template_uuid]
    ).where(tenant_tbl.c.sip_templates_generated.is_(True))

    return [
        row.global_trunk_sip_template_uuid
        for row in op.get_bind().execute(query)
    ]


def find_all_global_template_and_tenants():
    query = sa.sql.select(
        [tenant_tbl.c.uuid, tenant_tbl.c.global_sip_template_uuid]
    ).where(tenant_tbl.c.sip_templates_generated.is_(True))
    rows = op.get_bind().execute(query)
    return {row.uuid: row.global_sip_template_uuid for row in rows}


def find_trunk_tenants(trunks):
    query = sa.sql.select(
        [endpoint_sip_tbl.c.uuid, endpoint_sip_tbl.c.tenant_uuid],
    ).where(endpoint_sip_tbl.c.uuid.in_(trunks))
    rows = op.get_bind().execute(query)
    return {row.uuid: row.tenant_uuid for row in rows}


def rename_templates(template_uuids):
    query = endpoint_sip_tbl.update().values(
        label='registration_trunk',
    ).where(
        endpoint_sip_tbl.c.uuid.in_(template_uuids),
    )
    op.execute(query)


def rename_tenant_fk(old_name, new_name):
    old_fk_name = 'tenant_{}_fkey'.format(old_name)
    new_fk_name = 'tenant_{}_fkey'.format(new_name)
    table = 'tenant'
    op.alter_column(
        table,
        old_name,
        sa.ForeignKey(
            'endpoint_sip.uuid',
            ondelete='SET NULL',
            name=old_fk_name,
        ),
        new_column_name=new_name,
    )
    op.drop_constraint(
        constraint_name=old_fk_name,
        table_name=table,
        type_='foreignkey',
    )
    op.create_foreign_key(
        constraint_name=new_fk_name,
        source_table=table,
        referent_table='endpoint_sip',
        local_cols=[new_name],
        remote_cols=['uuid'],
    )


def list_registration_sections():
    query = sa.sql.select(

        [endpoint_sip_section_tbl.c.uuid]
    ).where(
        sa.and_(
            endpoint_sip_section_tbl.c.type == 'registration',
        )
    )
    rows = op.get_bind().execute(query)
    return [row.uuid for row in rows]


def list_endpoints_with_registration_section(all_registration_sections):
    query = sa.sql.select(
        [endpoint_sip_section_option_tbl.c.endpoint_sip_section_uuid]
    ).where(
        endpoint_sip_section_option_tbl.c.endpoint_sip_section_uuid.in_(
            all_registration_sections
        )
    ).distinct()
    rows = op.get_bind().execute(query)
    registration_sections_with_options = [row.endpoint_sip_section_uuid for row in rows]

    query = sa.sql.select(
        [endpoint_sip_section_tbl.c.endpoint_sip_uuid]
    ).where(
        endpoint_sip_section_tbl.c.uuid.in_(registration_sections_with_options)
    ).distinct()
    rows = op.get_bind().execute(query)
    return [row.endpoint_sip_uuid for row in rows]


def dissociate_endpoints_with_no_sections(to_dissociate, templates):
    query = endpoint_sip_template_tbl.delete().where(sa.and_(
        endpoint_sip_template_tbl.c.parent_uuid.in_(templates),
        endpoint_sip_template_tbl.c.child_uuid.in_(to_dissociate),
    ))
    op.execute(query)


def find_trunks_to_dissociate(endpoints_with_registrations, template_uuids):
    query = sa.sql.select(
        [endpoint_sip_template_tbl.c.child_uuid]
    ).where(sa.and_(
        endpoint_sip_template_tbl.c.parent_uuid.in_(template_uuids),
        ~endpoint_sip_template_tbl.c.child_uuid.in_(endpoints_with_registrations),
    )).distinct()
    rows = op.get_bind().execute(query)
    return [row.child_uuid for row in rows]


def remove_template_from_endpoint_without_registrations(template_uuids):
    registration_sections = list_registration_sections()
    endpoints_with_registrations = list_endpoints_with_registration_section(registration_sections)
    trunks_to_dissociate = find_trunks_to_dissociate(
        endpoints_with_registrations,
        template_uuids,
    )
    dissociate_endpoints_with_no_sections(trunks_to_dissociate, template_uuids)
    return trunks_to_dissociate


def associate_trunks_to_global_template(trunks):
    trunks_to_tenant = find_trunk_tenants(trunks)
    tenant_to_template = find_all_global_template_and_tenants()
    for trunk in trunks:
        tenant = trunks_to_tenant.get(trunk)
        template = tenant_to_template.get(tenant)
        if not template:
            continue

        query = endpoint_sip_template_tbl.insert().values(
            child_uuid=trunk,
            parent_uuid=template,
        )
        op.execute(query)


def upgrade():
    template_uuids = find_global_trunk_template_uuid()
    rename_templates(template_uuids)
    rename_tenant_fk(
        old_name='global_trunk_sip_template_uuid',
        new_name='registration_trunk_sip_template_uuid',
    )
    unassociated_trunks = remove_template_from_endpoint_without_registrations(template_uuids)
    associate_trunks_to_global_template(unassociated_trunks)


def downgrade():
    rename_tenant_fk(
        old_name='registration_trunk_sip_template_uuid',
        new_name='global_trunk_sip_template_uuid',
    )
