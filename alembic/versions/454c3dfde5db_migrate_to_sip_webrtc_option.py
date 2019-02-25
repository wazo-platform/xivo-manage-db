"""migrate_to_sip_webrtc_option

Revision ID: 454c3dfde5db
Revises: 7628599d48dc

"""

from alembic import op
from sqlalchemy import sql

# revision identifiers, used by Alembic.
revision = '454c3dfde5db'
down_revision = '7628599d48dc'

usersip_table = sql.table(
    'usersip',
    sql.column('id'),
    sql.column('encryption'),
    sql.column('options'),
)


def upgrade():
    query = (
        sql.select([usersip_table.c.id, usersip_table.c.options])
        .where(usersip_table.c.encryption == 1)
    )
    results = op.get_bind().execute(query).fetchall()

    for sip in results:
        old_webrtc_options = (
            ['avpf', 'yes'] in sip.options
            and ['dtlsenable', 'yes'] in sip.options
            and ['dtlssetup', 'actpass'] in sip.options
            and ['force_avp', 'yes'] in sip.options
            and ['icesupport', 'yes'] in sip.options
            and ['rtcp_mux', 'yes'] in sip.options
        )
        if not old_webrtc_options:
            continue

        sip.options.remove(['avpf', 'yes'])
        sip.options.remove(['dtlsenable', 'yes'])
        sip.options.remove(['dtlssetup', 'actpass'])
        sip.options.remove(['force_avp', 'yes'])
        sip.options.remove(['icesupport', 'yes'])
        sip.options.remove(['rtcp_mux', 'yes'])
        if ['webrtc', 'yes'] not in sip.options:
            sip.options.append(['webrtc', 'yes'])

        op.execute(
            usersip_table.update()
            .where(usersip_table.c.id == sip.id)
            .values(
                encryption=None,
                options=sip.options,
            )
        )


def downgrade():
    pass
