"""set taskpool_max_size

Revision ID: 38cc382d720f
Revises: f3bc803db64e

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = '38cc382d720f'
down_revision = 'f3bc803db64e'


asterisk_file = sa.sql.table(
    'asterisk_file',
    sa.sql.column('id'),
    sa.sql.column('name'),
)
asterisk_file_section = sa.sql.table(
    'asterisk_file_section',
    sa.sql.column('id'),
    sa.sql.column('name'),
    sa.sql.column('asterisk_file_id'),
)
asterisk_file_variable = sa.sql.table(
    'asterisk_file_variable',
    sa.sql.column('id'),
    sa.sql.column('key'),
    sa.sql.column('value'),
    sa.sql.column('asterisk_file_section_id'),
)

PJSIP_SYSTEM_SECTION_ID = (
    sa.select(asterisk_file_section.c.id)
    .where(asterisk_file_section.c.name == 'system')
    .where(
        asterisk_file_section.c.asterisk_file_id
        == sa.select(asterisk_file.c.id)
        .where(asterisk_file.c.name == 'pjsip.conf')
        .scalar_subquery()
    )
    .scalar_subquery()
)


def upgrade():
    conn = op.get_bind()

    exists = conn.execute(
        sa.select(asterisk_file_variable.c.id).where(
            asterisk_file_variable.c.key == 'taskpool_max_size',
            asterisk_file_variable.c.asterisk_file_section_id == PJSIP_SYSTEM_SECTION_ID,
        )
    ).fetchone()
    if exists:
        return

    conn.execute(
        asterisk_file_variable.insert().values(
            key='taskpool_max_size',
            value='100',
            asterisk_file_section_id=PJSIP_SYSTEM_SECTION_ID,
        )
    )


def downgrade():
    pass
