"""switch existing groups ignore_forward

See https://wazo-dev.atlassian.net/browse/WAZO-4169

Revision ID: aa8651c694fc
Revises: 0eb18070742c

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = 'aa8651c694fc'
down_revision = '0eb18070742c'


def upgrade():
    op.execute('UPDATE groupfeatures SET ignore_forward = 0 WHERE ignore_forward = 1')
    op.alter_column('groupfeatures', 'ignore_forward',
                    existing_type=sa.INTEGER(), server_default=sa.text('0'))

def downgrade():
    op.execute('UPDATE groupfeatures SET ignore_forward = 1 WHERE ignore_forward = 0')
    op.alter_column('groupfeatures', 'ignore_forward',
                    existing_type=sa.INTEGER(), server_default=sa.text('1'))
