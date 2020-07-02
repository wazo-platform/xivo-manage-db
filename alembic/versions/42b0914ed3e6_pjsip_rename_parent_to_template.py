"""pjsip-rename-parent-to-template

Revision ID: 42b0914ed3e6
Revises: ea74eca400ce

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = '42b0914ed3e6'
down_revision = 'ea74eca400ce'


def upgrade():
    op.rename_table('endpoint_sip_parent', 'endpoint_sip_template')


def downgrade():
    op.rename_table('endpoint_sip_template', 'endpoint_sip_parent')
