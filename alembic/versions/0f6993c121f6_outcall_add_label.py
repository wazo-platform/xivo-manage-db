"""outcall add label

Revision ID: 0f6993c121f6
Revises: 8fe383847bcc

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f6993c121f6'
down_revision = '8fe383847bcc'

outcall_tbl = sa.sql.table(
    'outcall',
    sa.sql.column('id'),
    sa.sql.column('name'),
    sa.sql.column('label'),
)


def upgrade():
    op.add_column(
        'outcall',
        sa.Column('label', sa.Text),
    )
    query = outcall_tbl.update().values(label=outcall_tbl.c.name)
    op.execute(query)
    op.alter_column('outcall', 'label', nullable=False)


def downgrade():
    op.drop_column('outcall', 'label')
