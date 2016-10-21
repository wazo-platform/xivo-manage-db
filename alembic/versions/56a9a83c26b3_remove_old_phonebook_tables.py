"""remove old phonebook tables

Revision ID: 56a9a83c26b3
Revises: 21d45c24210e

"""

# revision identifiers, used by Alembic.
revision = '56a9a83c26b3'
down_revision = '21d45c24210e'

from alembic import op


def upgrade():
    op.drop_table('user_contact')
    op.drop_table('phonebooknumber')
    op.drop_table('phonebookaddress')
    op.drop_table('phonebook')


def downgrade():
    pass
