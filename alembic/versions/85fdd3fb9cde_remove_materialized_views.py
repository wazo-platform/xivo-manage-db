"""remove materialized views

Revision ID: 85fdd3fb9cde
Revises: e8ef1a06f16f

"""

from alembic import op
from sqlalchemy_utils.view import DropView


# revision identifiers, used by Alembic.
revision = '85fdd3fb9cde'
down_revision = 'e8ef1a06f16f'


def upgrade():
    op.drop_index('endpoint_sip_options_view__idx_root', 'endpoint_sip_options_view')
    op.execute(DropView('endpoint_sip_options_view', materialized=True))


def downgrade():
    pass
