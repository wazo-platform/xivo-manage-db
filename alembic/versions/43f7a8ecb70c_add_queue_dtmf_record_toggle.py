"""add queue dtmf_record_toggle

Revision ID: 43f7a8ecb70c
Revises: d8e7dcde9c9f

"""

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '43f7a8ecb70c'
down_revision = 'd8e7dcde9c9f'

TBL_NAME = 'queuefeatures'
COL_NAME = 'dtmf_record_toggle'


def upgrade():
    op.add_column(
        TBL_NAME,
        sa.Column(
            COL_NAME,
            sa.Boolean,
            nullable=False,
            server_default=sa.text('true'),
        ),
    )


def downgrade():
    op.drop_column(TBL_NAME, COL_NAME)
