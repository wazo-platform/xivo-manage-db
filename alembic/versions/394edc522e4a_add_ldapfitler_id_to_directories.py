"""add ldapfitler_id to directories

Revision ID: 394edc522e4a
Revises: 30eebcef63ad

"""

# revision identifiers, used by Alembic.
revision = '394edc522e4a'
down_revision = '30eebcef63ad'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('directories',
                  sa.Column('ldapfilter_id',
                             sa.Integer,
                             sa.ForeignKey('ldapfilter.id', ondelete='CASCADE'),
                             nullable=True))


def downgrade():
    op.drop_column('directories', 'ldapfilter_id')
