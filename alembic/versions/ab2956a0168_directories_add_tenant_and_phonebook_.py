"""directories_add_tenant_and_phonebook_fields

Revision ID: ab2956a0168
Revises: 1aef8dfb5a12

"""

# revision identifiers, used by Alembic.
revision = 'ab2956a0168'
down_revision = '1aef8dfb5a12'

from alembic import op
import sqlalchemy as sa

t = 'directories'
columns = ['dird_tenant', 'dird_phonebook']


def upgrade():
    for c in columns:
        op.add_column(t, sa.Column(c, sa.Text))


def downgrade():
    for c in columns:
        op.drop_column(t, c)
