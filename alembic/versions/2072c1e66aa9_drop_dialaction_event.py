"""drop dialaction_event

Revision ID: 2072c1e66aa9
Revises: 2fbbd4231cca

"""

# revision identifiers, used by Alembic.
revision = '2072c1e66aa9'
down_revision = '2fbbd4231cca'

from alembic import op
from sqlalchemy.types import String


def upgrade():
    _drop_dialaction_event()


def _drop_dialaction_event():
    op.alter_column('dialaction', 'event', type_=String(40))
    op.execute('DROP TYPE dialaction_event')


def downgrade():
    pass
