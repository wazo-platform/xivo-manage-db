"""add a source field to all sources

Revision ID: b2abcc84ad
Revises: 592e449b34ec

"""

# revision identifiers, used by Alembic.
revision = 'b2abcc84ad'
down_revision = '592e449b34ec'

from alembic import op
from sqlalchemy import sql, and_

fields_table = sql.table('ctidirectoryfields',
                         sql.column('dir_id'),
                         sql.column('fieldname'),
                         sql.column('value'))
cti_directories_table = sql.table('ctidirectories',
                                  sql.column('id'),
                                  sql.column('description'))


def upgrade():
    conn = op.get_bind()
    rows = conn.execute(sql.select([cti_directories_table]).
                        where(cti_directories_table.c.description != ''))
    for dir_id, description in rows:
        rows = conn.execute(sql.select([fields_table.c.dir_id])
                            .where(and_(fields_table.c.dir_id == dir_id,
                                        fields_table.c.fieldname == 'source')))
        if rows.rowcount:
            continue
        op.execute(fields_table.insert().values(dir_id=dir_id,
                                                fieldname='source',
                                                value=description))


def downgrade():
    pass
