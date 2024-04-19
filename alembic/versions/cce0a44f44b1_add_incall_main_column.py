"""add-incall-main-column

Revision ID: cce0a44f44b1
Revises: b38ce53a1d32

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'cce0a44f44b1'
down_revision = 'b38ce53a1d32'

incall_tbl = sa.sql.table(
    'incall',
    sa.sql.column('id'),
    sa.sql.column('main'),
    sa.sql.column('tenant_uuid'),
)


def upgrade():
    op.add_column(
        'incall',
        sa.Column(
            'main',
            sa.Boolean,
            nullable=True,
            server_default='false',
        ),
    )

    # Migrate the lowest ID from each tenant to be the main incall
    min_ids_by_tenant = (
        sa.sql.select([sa.func.min(incall_tbl.c.id)])
        .group_by(incall_tbl.c.tenant_uuid)
        .alias()
    )
    update_query = (
        incall_tbl
        .update()
        .where(incall_tbl.c.id.in_(min_ids_by_tenant))
        .values(main=True)
    )
    op.execute(update_query)


def downgrade():
    op.drop_column('incall', 'main')
