"""add-context-id

Revision ID: 18b419c519f4
Revises: 9142f0403c8

"""

# revision identifiers, used by Alembic.
revision = '18b419c519f4'
down_revision = '9142f0403c8'

from alembic import op


def upgrade():
    op.drop_constraint('context_pkey', 'context')
    op.execute('ALTER TABLE context ADD COLUMN id SERIAL;')
    op.create_primary_key('context_pkey', 'context', ['id'])
    op.create_unique_constraint('context_name', 'context', ['name'])
    op.alter_column('context', 'description', nullable=True)
    op.alter_column('context', 'displayname', nullable=True, server_default=None)


def downgrade():
    op.alter_column('context', 'displayname', nullable=False, server_default='')
    op.alter_column('context', 'description', nullable=False)
    op.drop_constraint('context_name', 'context')
    op.drop_constraint('context_pkey', 'context')
    op.drop_column('context', 'id')
    op.create_primary_key('context_pkey', 'context', ['name'])
