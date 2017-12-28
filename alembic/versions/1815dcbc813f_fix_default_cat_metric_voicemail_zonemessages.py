"""fix_default_voicemail_zonemessages

Revision ID: 1815dcbc813f
Revises: 14c0ca8a7834

"""

# revision identifiers, used by Alembic.
revision = '1815dcbc813f'
down_revision = '14c0ca8a7834'

from alembic import op
import sqlalchemy as sa

staticvoicemail = sa.sql.table('staticvoicemail',
                               sa.sql.column('cat_metric'),
                               sa.sql.column('category'))


def upgrade():
    query = (staticvoicemail
             .update()
             .where(staticvoicemail.c.category == 'zonemessages')
             .values(cat_metric=1))
    op.execute(query)


def downgrade():
    pass
