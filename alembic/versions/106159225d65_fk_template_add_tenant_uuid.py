"""fk_template_add_tenant_uuid

Revision ID: 106159225d65
Revises: 5c9f286599b6

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '106159225d65'
down_revision = '5c9f286599b6'


func_key_template_tbl = sa.sql.table(
    'func_key_template',
    sa.sql.column('id'),
    sa.sql.column('tenant_uuid'),
)
func_key_mapping_tbl = sa.sql.table(
    'func_key_mapping',
    sa.sql.column('template_id'),
)
userfeatures_tbl = sa.sql.table(
    'userfeatures',
    sa.sql.column('tenant_uuid'),
    sa.sql.column('func_key_template_id'),
    sa.sql.column('func_key_private_template_id'),
)
tenant_tbl = sa.sql.table('tenant', sa.sql.column('uuid'))


def associate_tenants():
    # associate tenant to public templates
    filter_ = userfeatures_tbl.c.func_key_template_id == func_key_template_tbl.c.id
    public_sub_query = (
        sa.sql.select([userfeatures_tbl.c.func_key_template_id])
        .where(filter_)
        .limit(1)
    )
    public_query = (
        sa.sql.select([userfeatures_tbl.c.tenant_uuid])
        .where(filter_)
        .limit(1)
    )
    query = (
        func_key_template_tbl
        .update()
        .where(func_key_template_tbl.c.id.in_(public_sub_query))
        .values(tenant_uuid=public_query)
    )
    op.execute(query)

    # associate tenant to private templates
    filter_ = userfeatures_tbl.c.func_key_private_template_id == func_key_template_tbl.c.id
    private_sub_query = (
        sa.sql.select([userfeatures_tbl.c.func_key_private_template_id])
        .where(filter_)
        .limit(1)
    )
    private_query = (
        sa.sql.select([userfeatures_tbl.c.tenant_uuid])
        .where(filter_)
        .limit(1)
    )
    query = (
        func_key_template_tbl
        .update()
        .where(func_key_template_tbl.c.id.in_(private_sub_query))
        .values(tenant_uuid=private_query)
    )
    op.execute(query)

    # Remove unassociated templates
    sub_query = (
        sa.sql.select([func_key_template_tbl.c.id])
        .where(func_key_template_tbl.c.tenant_uuid == None)  # noqa
    )
    query = (
        func_key_mapping_tbl.delete()
        .where(func_key_mapping_tbl.c.template_id.in_(sub_query))
    )
    op.execute(query)

    query = (
        func_key_template_tbl.delete()
        .where(func_key_template_tbl.c.tenant_uuid == None)  # noqa
    )
    op.execute(query)


def upgrade():
    op.add_column(
        'func_key_template',
        sa.Column(
            'tenant_uuid',
            sa.String(36),
            sa.ForeignKey('tenant.uuid', ondelete='CASCADE'),
            nullable=True,
        )
    )

    associate_tenants()

    op.alter_column('func_key_template', 'tenant_uuid', nullable=False)


def downgrade():
    op.drop_column('func_key_template', 'tenant_uuid')
