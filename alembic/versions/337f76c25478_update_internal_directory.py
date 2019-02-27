"""update internal directory

Revision ID: 337f76c25478
Revises: 20debb21dc01

"""

# revision identifiers, used by Alembic.
revision = '337f76c25478'
down_revision = '20debb21dc01'

from alembic import op
from sqlalchemy import sql, and_, or_

fields_table = sql.table('ctidirectoryfields',
                         sql.column('dir_id'),
                         sql.column('fieldname'),
                         sql.column('value'))
directories = sql.table('ctidirectories',
                        sql.column('id'),
                        sql.column('uri'),
                        sql.column('match_direct'),
                        sql.column('match_reverse'))


def _clean(field):
    return field.replace('userfeatures.', '').replace('extensions.', '')


def _update_fields(conn):
    rows = conn.execute(sql.select([fields_table.c.dir_id,
                                    fields_table.c.fieldname,
                                    fields_table.c.value])
                        .where(or_(fields_table.c.value.like('{userfeatures.%}'),
                                   fields_table.c.value.like('{extensions.%}'))))
    for row in rows:
        op.execute(fields_table
                   .update()
                   .where(and_(fields_table.c.dir_id == row.dir_id,
                               fields_table.c.fieldname == row.fieldname))
                   .values(value=_clean(row.value)))


def _update_directories(conn):
    rows = conn.execute(sql.select([directories])
                        .where(directories.c.uri == 'http://localhost:9487'))
    configs = {row.id: {'match_direct': row.match_direct,
                        'match_reverse': row.match_reverse} for row in rows}
    for id_, config in configs.items():
        op.execute(directories.update()
                   .where(directories.c.id == id_)
                   .values(match_direct=_clean(config['match_direct']),
                           match_reverse=_clean(config['match_reverse'])))


def upgrade():
    conn = op.get_bind()
    _update_fields(conn)
    _update_directories(conn)


def downgrade():
    pass
