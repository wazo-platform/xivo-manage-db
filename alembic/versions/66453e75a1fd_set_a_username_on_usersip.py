"""set a username on usersip

Revision ID: 66453e75a1fd
Revises: c3ecaf2f9e78

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66453e75a1fd'
down_revision = 'c3ecaf2f9e78'

usersip_table = sa.sql.table(
    'usersip',
    sa.sql.column('name'),
    sa.sql.column('username'),
)


def upgrade():
    op.execute(
        usersip_table.update().values(
            username=usersip_table.c.name
        ).where(usersip_table.c.username == None)
    )


def downgrade():
    pass
