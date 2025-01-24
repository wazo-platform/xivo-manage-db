"""change group and queue default toggle record to off

Revision ID: 3d1087b7867b
Revises: 6aec6d04fc29

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = '3d1087b7867b'
down_revision = '6aec6d04fc29'


def upgrade():
    op.alter_column(
        'groupfeatures',
        'dtmf_record_toggle',
        server_default=sa.text('false'),
    )
    op.alter_column(
        'queuefeatures',
        'dtmf_record_toggle',
        server_default=sa.text('false'),
    )


def downgrade():
    op.alter_column(
        'groupfeatures',
        'dtmf_record_toggle',
        server_default=sa.text('true'),
    )
    op.alter_column(
        'queuefeatures',
        'dtmf_record_toggle',
        server_default=sa.text('true'),
    )
