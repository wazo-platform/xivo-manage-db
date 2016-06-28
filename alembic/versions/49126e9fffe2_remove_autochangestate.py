"""remove autochangestate

Revision ID: 49126e9fffe2
Revises: 564d634619bc

"""

# revision identifiers, used by Alembic.
revision = '49126e9fffe2'
down_revision = '564d634619bc'

from alembic import op
import sqlalchemy as sa

preference_table = sa.sql.table('cti_preference',
                                sa.sql.column('id'),
                                sa.sql.column('option'))


def upgrade():
    op.execute(preference_table.delete().where(preference_table.c.option == 'presence.autochangestate'))


def downgrade():
    op.execute(preference_table.insert().values(option='presence.autochangestate'))
