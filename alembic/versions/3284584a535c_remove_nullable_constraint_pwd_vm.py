"""remove_nullable_constraint_pwd_vm

Revision ID: 3284584a535c
Revises: 58d561775bf3

"""

# revision identifiers, used by Alembic.
revision = '3284584a535c'
down_revision = '58d561775bf3'

from alembic import op


def upgrade():
    op.alter_column('voicemail', 'password', nullable=True, server_default=None)


def downgrade():
    op.alter_column('voicemail', 'password', nullable=False, server_default='')
