"""add-group-label

Revision ID: 4d539700bb90
Revises: 757111d049b6

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d539700bb90'
down_revision = '757111d049b6'

groupfeatures_tbl = sa.sql.table(
    'groupfeatures',
    sa.sql.column('uuid'),
    sa.sql.column('name'),
    sa.sql.column('label'),
)


def upgrade():
    op.add_column(
        'groupfeatures',
        sa.Column('label', sa.Text),
    )
    query = groupfeatures_tbl.update().values(label=groupfeatures_tbl.c.name)
    op.execute(query)
    op.alter_column('groupfeatures', 'label', nullable=False)


def downgrade():
    op.drop_column('groupfeatures', 'label')
