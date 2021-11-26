"""fix queuemember interfaces

Revision ID: 29290c38946f
Revises: 241501a5f8ba

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29290c38946f'
down_revision = '241501a5f8ba'


queuemember_tbl = sa.sql.table(
    'queuemember',
    sa.sql.column('interface'),
    sa.sql.column('channel'),
)


def upgrade():
    op.execute(
        queuemember_tbl
        .update()
        .where(queuemember_tbl.c.channel == 'SIP')
        .values(interface='PJ' + queuemember_tbl.c.interface)
    )


def downgrade():
    pass
