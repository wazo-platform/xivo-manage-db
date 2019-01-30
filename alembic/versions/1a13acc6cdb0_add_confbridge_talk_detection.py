"""add confbridge talk detection

Revision ID: 1a13acc6cdb0
Revises: 5dd4a73c91c2

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy import sql


# revision identifiers, used by Alembic.
revision = '1a13acc6cdb0'
down_revision = '5dd4a73c91c2'

asterisk_file_table = sa.sql.table('asterisk_file',
                                   sa.sql.column('id'),
                                   sa.sql.column('name'))

asterisk_file_section_table = sa.sql.table('asterisk_file_section',
                                           sa.sql.column('id'),
                                           sa.sql.column('name'),
                                           sa.sql.column('priority'),
                                           sa.sql.column('asterisk_file_id'))

asterisk_file_variable_table = sa.sql.table('asterisk_file_variable',
                                            sa.sql.column('id'),
                                            sa.sql.column('key'),
                                            sa.sql.column('value'),
                                            sa.sql.column('priority'),
                                            sa.sql.column('asterisk_file_section_id'))


def upgrade():
    section_id = _find_asterisk_file_section('confbridge.conf', 'wazo_default_user')
    if not _find_asterisk_file_variable(section_id, 'talk_detection_events'):
        _insert_asterisk_file_variable(section_id, 'talk_detection_events', 'yes')


def _find_asterisk_file_section(file_name, section_name):
    query = (
        sql.select([asterisk_file_section_table.c.id],
                   from_obj=[asterisk_file_section_table.join(
                       asterisk_file_table,
                       asterisk_file_table.c.id == asterisk_file_section_table.c.asterisk_file_id
                   )]
        ).where(sql.and_(
            asterisk_file_table.c.name == file_name,
            asterisk_file_section_table.c.name == section_name,
        ))
    )
    return op.get_bind().execute(query).scalar()


def _find_asterisk_file_variable(section_id, variable):
    query = (
        sql.select([sa.func.count(asterisk_file_variable_table.c.id)])
        .where(
            asterisk_file_variable_table.c.key == variable,
        )
    )
    return op.get_bind().execute(query).scalar() > 0


def _insert_asterisk_file_variable(section_id, key, value):
    query = (asterisk_file_variable_table
             .insert()
             .values(key=key,
                     value=value,
                     asterisk_file_section_id=section_id))
    op.get_bind().execute(query)


def downgrade():
    pass
