"""remove-usersip-table

Revision ID: 9ce1ffce9f15
Revises: 30fc2693c6fc

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = '9ce1ffce9f15'
down_revision = '30fc2693c6fc'


def upgrade():
    # Drop unused ENUM
    op.execute('DROP TYPE usersip_protocol')
    op.execute('DROP TYPE useriax_protocol')

    # Drop unused usersip and associated ENUM
    op.drop_table('usersip')
    op.execute('DROP TYPE usersip_dtmfmode')
    op.execute('DROP TYPE usersip_insecure')
    op.execute('DROP TYPE usersip_nat')
    op.execute('DROP TYPE usersip_progressinband')
    op.execute('DROP TYPE usersip_session_refresher')
    op.execute('DROP TYPE usersip_session_timers')
    op.execute('DROP TYPE usersip_videosupport')


def downgrade():
    pass
