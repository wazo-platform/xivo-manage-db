"""move column merging from display to directories

Revision ID: 20debb21dc01
Revises: b2abcc84ad

"""

# revision identifiers, used by Alembic.
revision = '20debb21dc01'
down_revision = 'b2abcc84ad'

import json
import re

from alembic import op
from sqlalchemy import sql, and_
from unidecode import unidecode

cti_contexts = sql.table('cticontexts',
                         sql.column('id'),
                         sql.column('name'),
                         sql.column('directories'),
                         sql.column('display'))
cti_displays = sql.table('ctidisplays',
                         sql.column('id'),
                         sql.column('name'),
                         sql.column('data'))
cti_directories = sql.table('ctidirectories',
                            sql.column('id'),
                            sql.column('name'))
cti_directory_fields = sql.table('ctidirectoryfields',
                                 sql.column('dir_id'),
                                 sql.column('fieldname'),
                                 sql.column('value'))


def _get_display_config(display):
    return json.loads(display.data) if display.data else {}


def _find_formatted_fields(config):
    formatted_fields = []
    for pos, (name, _, _, field) in config.iteritems():
        if field and not field.isalpha():
            formatted_fields.append((name, pos, field))
    return formatted_fields


def _source_using_display(conn, display_name):
    source_names = set()
    rows = conn.execute(sql.select([cti_contexts])
                        .where(and_(cti_contexts.c.display == display_name,
                                    cti_contexts.c.directories != '')))
    for row in rows:
        for name in row.directories.split(','):
            source_names.add(name)

    return list(source_names)


def _update_sources(conn, column_info):
    rows = conn.execute(sql.select([cti_directories.c.id])
                           .where(cti_directories.c.name.in_(column_info['sources'])))
    for row in rows:
        already_there = conn.execute(
            sql.select([cti_directory_fields.c.dir_id])
            .where(and_(cti_directory_fields.c.dir_id == row.id,
                        cti_directory_fields.c.fieldname == column_info['source_col']))).rowcount != 0
        if already_there:
            continue
        fields = conn.execute(sql.select([cti_directory_fields.c.fieldname,
                                          cti_directory_fields.c.value])
                              .where(cti_directory_fields.c.dir_id == row.id))

        source_fields = column_info['source_fields']
        for field in fields:
            old_field = '{%s}' % field.fieldname
            new_field = field.value
            source_fields = source_fields.replace(old_field, new_field)

        op.execute(cti_directory_fields.insert().values(dir_id=row.id,
                                                        fieldname=column_info['source_col'],
                                                        value=source_fields))


def _update_display(conn, column_info):
    new_data = column_info['display_data']
    pos = column_info['position']
    title, type_, default, _ = column_info['display_data'][pos]
    new_data[pos] = title, type_, default, column_info['source_col']
    op.execute(cti_displays
               .update()
               .where(cti_displays.c.name == column_info['display'])
               .values(data=json.dumps(new_data)))


def _get_column_to_migrate(conn):
    r = re.compile(r'(\W*)(\w+)(\W*)')
    rows = conn.execute(sql.select([cti_displays]))
    to_migrate = []
    for row in rows:
        config = _get_display_config(row)
        to_move = _find_formatted_fields(config)
        if not to_move:
            continue
        source_names = _source_using_display(conn, row.name)
        for name, pos, field in to_move:
            source_column = unidecode(name.lower().replace(' ', '_'))
            source_format = r.sub(r'\1{\2}\3', field)
            to_migrate.append({'display': row.name,
                               'position': pos,
                               'source_col': source_column,
                               'source_fields': source_format,
                               'sources': source_names,
                               'display_data': config})
    return to_migrate


def upgrade():
    conn = op.get_bind()
    to_migrate = _get_column_to_migrate(conn)
    for column_info in to_migrate:
        _update_sources(conn, column_info)
        _update_display(conn, column_info)


def downgrade():
    pass
