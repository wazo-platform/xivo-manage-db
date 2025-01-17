"""add_group_dtmf_record_toggle

Revision ID: 6aec6d04fc29
Revises: 58b1be9f53cd

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = '6aec6d04fc29'
down_revision = '58b1be9f53cd'


TBL_NAME = 'groupfeatures'
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
