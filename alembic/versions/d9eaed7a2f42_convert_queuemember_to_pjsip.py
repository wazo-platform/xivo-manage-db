"""convert_queuemember_to_pjsip

Revision ID: d9eaed7a2f42
Revises: ba7c6bb897b3

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'd9eaed7a2f42'
down_revision = 'ba7c6bb897b3'

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
