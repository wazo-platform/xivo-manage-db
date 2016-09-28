"""delete sessions

Revision ID: 30eebcef63ad
Revises: ab2956a0168

"""

# revision identifiers, used by Alembic.
revision = '30eebcef63ad'
down_revision = 'ab2956a0168'

from alembic import op
from sqlalchemy import sql

session = sql.table('session')


def upgrade():
    op.execute(session.delete())


def downgrade():
    pass
