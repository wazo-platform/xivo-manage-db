"""queueskillrule add tenant_uuid

Revision ID: 73889d1db031
Revises: 0aeb61795700

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73889d1db031'
down_revision = '0aeb61795700'

queueskillrule_tbl = sa.sql.table(
    'queueskillrule',
    sa.sql.column('id'),
    sa.sql.column('name'),
    sa.sql.column('rule'),
    sa.sql.column('tenant_uuid'),
)


def delete_all():
    query = queueskillrule_tbl.delete()
    op.execute(query)


def upgrade():
    delete_all()

    op.add_column(
        'queueskillrule',
        sa.Column(
            'tenant_uuid',
            sa.String(36),
            sa.ForeignKey('tenant.uuid', ondelete='CASCADE'),
            nullable=False
        )
    )


def downgrade():
    op.drop_column('queueskillrule', 'tenant_uuid')
