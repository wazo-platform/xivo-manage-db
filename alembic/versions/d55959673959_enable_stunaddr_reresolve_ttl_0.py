"""enable stunaddr_reresolve_ttl_0 in rtp.conf

Revision ID: d55959673959
Revises: 091ab2e3ff4d

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'd55959673959'
down_revision = '091ab2e3ff4d'

KEY = 'stunaddr_reresolve_ttl_0'
VALUE = 'yes'

asterisk_file_table = sa.sql.table(
    'asterisk_file',
    sa.sql.column('id'),
    sa.sql.column('name'),
)

asterisk_file_section_table = sa.sql.table(
    'asterisk_file_section',
    sa.sql.column('id'),
    sa.sql.column('name'),
    sa.sql.column('asterisk_file_id'),
)

asterisk_file_variable_table = sa.sql.table(
    'asterisk_file_variable',
    sa.sql.column('id'),
    sa.sql.column('key'),
    sa.sql.column('value'),
    sa.sql.column('asterisk_file_section_id'),
)


def _rtp_general_section_id(conn):
    file_id = conn.execute(
        sa.select([asterisk_file_table.c.id])
        .where(asterisk_file_table.c.name == 'rtp.conf')
    ).scalar()
    if file_id is None:
        return None
    return conn.execute(
        sa.select([asterisk_file_section_table.c.id])
        .where(
            sa.and_(
                asterisk_file_section_table.c.name == 'general',
                asterisk_file_section_table.c.asterisk_file_id == file_id,
            )
        )
    ).scalar()


def upgrade():
    conn = op.get_bind()
    section_id = _rtp_general_section_id(conn)
    if section_id is None:
        return

    already_set = conn.execute(
        sa.select([asterisk_file_variable_table.c.id])
        .where(
            sa.and_(
                asterisk_file_variable_table.c.key == KEY,
                asterisk_file_variable_table.c.asterisk_file_section_id == section_id,
            )
        )
    ).scalar()
    if already_set is not None:
        return

    conn.execute(
        asterisk_file_variable_table.insert().values(
            key=KEY,
            value=VALUE,
            asterisk_file_section_id=section_id,
        )
    )


def downgrade():
    conn = op.get_bind()
    section_id = _rtp_general_section_id(conn)
    if section_id is None:
        return

    conn.execute(
        asterisk_file_variable_table.delete().where(
            sa.and_(
                asterisk_file_variable_table.c.key == KEY,
                asterisk_file_variable_table.c.asterisk_file_section_id == section_id,
            )
        )
    )
