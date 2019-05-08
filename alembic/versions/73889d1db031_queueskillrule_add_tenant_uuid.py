"""queueskillrule add tenant_uuid

Revision ID: 73889d1db031
Revises: 0aeb61795700

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73889d1db031'
down_revision = '0aeb61795700'

queueskillrule_tbl = sa.sql.table('queueskillrule', sa.sql.column('tenant_uuid'))
queuefeatures_tbl = sa.sql.table('queuefeatures', sa.sql.column('tenant_uuid'))


def associate_tenants():
    query = sa.sql.select([queuefeatures_tbl.c.tenant_uuid])
    result = op.get_bind().execute(query).first()

    if result:
        tenant_uuid = result[0]
        query = (
            queueskillrule_tbl.update()
            .values(tenant_uuid=tenant_uuid)
        )
        op.execute(query)
    else:
        query = queueskillrule_tbl.delete()
        op.execute(query)


def upgrade():
    op.add_column(
        'queueskillrule',
        sa.Column(
            'tenant_uuid',
            sa.String(36),
            sa.ForeignKey('tenant.uuid', ondelete='CASCADE'),
            nullable=True
        )
    )

    associate_tenants()

    op.alter_column('queueskillrule', 'tenant_uuid', nullable=False)


def downgrade():
    op.drop_column('queueskillrule', 'tenant_uuid')
