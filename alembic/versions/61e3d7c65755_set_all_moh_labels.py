"""set all moh labels

Revision ID: 61e3d7c65755
Revises: da06cfd76289

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61e3d7c65755'
down_revision = 'da06cfd76289'


def upgrade():
    moh = sa.sql.table(
        'moh',
        sa.sql.column('name'),
        sa.sql.column('label'),
    )
    op.execute(
        moh.update().values(label=moh.c.name).where(moh.c.label.is_(None))
    )
    op.alter_column('moh', 'label', nullable=False)


def downgrade():
    op.alter_column('moh', 'label', nullable=True)
