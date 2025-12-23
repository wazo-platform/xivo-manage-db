"""remove materialized views

Revision ID: 85fdd3fb9cde
Revises: fb097e414392

"""

from alembic import op
from sqlalchemy_utils.view import DropView


# revision identifiers, used by Alembic.
revision = '85fdd3fb9cde'
down_revision = 'fb097e414392'


def upgrade():
    op.drop_index('endpoint_sip_options_view__idx_root', 'endpoint_sip_options_view')
    op.execute(DropView('endpoint_sip_options_view', materialized=True))


def downgrade():
    pass
