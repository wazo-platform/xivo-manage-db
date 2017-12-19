"""remove paging.callnotbusy column

Revision ID: 438cb372df48
Revises: 55f7b6c13454

"""

# revision identifiers, used by Alembic.
revision = '438cb372df48'
down_revision = '55f7b6c13454'

from alembic import op


def upgrade():
    connection = op.get_bind()
    query = 'ALTER TABLE "paging" DROP COLUMN IF EXISTS "callnotbusy"'
    connection.execute(query)


def downgrade():
    '''
    This migration fixes a desync between installed/migrated schema introduced
    in 12.23. No downgrade supported.
    '''
    pass
