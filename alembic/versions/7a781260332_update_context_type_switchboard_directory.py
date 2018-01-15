"""update_context_type_switchboard_directory

Revision ID: 7a781260332
Revises: 5085447dd295

"""

# revision identifiers, used by Alembic.
revision = '7a781260332'
down_revision = '5085447dd295'

from alembic import op
import sqlalchemy as sa

context = sa.sql.table(
    'context',
    sa.Column('name'),
    sa.Column('contexttype'),
)


def upgrade():
    op.execute(context
               .update()
               .where(context.c.name == '__switchboard_directory')
               .values(contexttype='services'))


def downgrade():
    op.execute(context
               .update()
               .where(context.c.name == '__switchboard_directory')
               .values(contexttype='internal'))
