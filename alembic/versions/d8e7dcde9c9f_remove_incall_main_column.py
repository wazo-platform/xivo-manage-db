"""remove incall 'main' column

Revision ID: d8e7dcde9c9f
Revises: 00ae4937814f

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8e7dcde9c9f'
down_revision = '00ae4937814f'

incall_tbl = sa.sql.table(
    'incall',
    sa.sql.column('id'),
    sa.sql.column('main'),
    sa.sql.column('tenant_uuid'),
)

def upgrade():
    op.drop_column('incall', 'main')

def downgrade():
    # logic taken from rev. cce0a44f44b1_add_incall_main_column.py
    op.add_column(
        'incall',
        sa.Column(
            'main',
            sa.Boolean,
            nullable=False,
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
