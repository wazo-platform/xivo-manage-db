"""call_filter add label column

Revision ID: 8353aca45dcb
Revises: 1ec7cdef9eeb

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8353aca45dcb'
down_revision = '1ec7cdef9eeb'


callfilter_tbl = sa.sql.table(
    'callfilter',
    sa.sql.column('name'),
    sa.sql.column('label'),
)


def upgrade():
    op.add_column(
        'callfilter',
        sa.Column('label', sa.Text),
    )
    query = callfilter_tbl.update().values(label=callfilter_tbl.c.name)
    op.execute(query)
    op.alter_column('callfilter', 'label', nullable=False)


def downgrade():
    op.drop_column('callfilter', 'label')
