"""refactor queue table

Revision ID: 4cf42964a0f8
Revises: 3131b2ccb06f

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = '4cf42964a0f8'
down_revision = '3131b2ccb06f'


def upgrade():
    op.rename_table('queue', 'base_queue')
    op.create_check_constraint(
        'base_queue_autopause_check',
        'base_queue',
        "autopause in ('no', 'yes', 'all')",
    )
    op.drop_constraint('queue_autopause_check', 'base_queue')
    op.drop_constraint('queue_pkey', 'base_queue')
    op.create_primary_key(
        'base_queue_pkey',
        'base_queue',
        ['name'],
    )


def downgrade():
    op.rename_table('base_queue', 'queue')
    op.create_check_constraint(
        'queue_autopause_check',
        'queue',
        "autopause in ('no', 'yes', 'all')",
    )
    op.drop_constraint('base_queue_autopause_check', 'queue')
    op.drop_constraint('base_queue_pkey', 'queue')
    op.create_primary_key(
        'queue_pkey',
        'queue',
        ['name'],
    )
