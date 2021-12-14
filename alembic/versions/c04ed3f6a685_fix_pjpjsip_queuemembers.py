"""fix PJPJSIP queuemembers

Revision ID: c04ed3f6a685
Revises: 785b8cb74daa

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c04ed3f6a685'
down_revision = '785b8cb74daa'

queuemember_tbl = sa.sql.table(
    'queuemember',
    sa.sql.column('interface'),
    sa.sql.column('channel'),
)


def upgrade():
    op.execute(
        queuemember_tbl
        .update()
        .where(
            sa.and_(
                queuemember_tbl.c.channel == 'SIP',
                queuemember_tbl.c.interface.startswith('PJPJSIP/'),
            )
        )
        .values(interface=sa.func.replace(queuemember_tbl.c.interface, 'PJPJSIP', 'PJSIP'))
    )


def downgrade():
    pass
