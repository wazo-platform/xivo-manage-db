"""remove-deprecated-incall-fields

Revision ID: 203f6f2cf0a0
Revises: 2bb55c201ee7

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '203f6f2cf0a0'
down_revision = '2bb55c201ee7'


def upgrade():
    op.drop_column('incall', 'exten')
    op.drop_column('incall', 'context')


def downgrade():
    op.add_column('incall', sa.Column('exten', sa.String(40)))
    op.add_column('incall', sa.Column('context', sa.String(39)))
    op.create_unique_constraint(
        'incall_exten_context_key',
        'incall',
        ['exten', 'context'],
    )
    op.create_index(
        index_name='incall__idx__context',
        table_name='incall',
        columns=['context'],
    )
    op.create_index(
        index_name='incall__idx__exten',
        table_name='incall',
        columns=['exten'],
    )
