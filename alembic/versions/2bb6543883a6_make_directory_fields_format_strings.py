"""Make cti directory fields format strings

Revision ID: 2bb6543883a6
Revises: 444b39e9aa32

"""

# revision identifiers, used by Alembic.
revision = '2bb6543883a6'
down_revision = '444b39e9aa32'

from alembic import op
from sqlalchemy import sql, and_

fields_table = sql.table('ctidirectoryfields',
                         sql.column('dir_id'),
                         sql.column('fieldname'),
                         sql.column('value'))


def upgrade():
    conn = op.get_bind()
    rows = conn.execute(sql.select([fields_table.c.dir_id,
                                    fields_table.c.fieldname,
                                    fields_table.c.value]).where(~fields_table.c.value.like('{%}')))
    to_upgrade = {(row.dir_id, row.fieldname): row.value for row in rows}
    for (dir_id, fieldname), value in to_upgrade.items():
        new_value = '{%s}' % '} {'.join(value.split(' '))
        op.execute(fields_table
                   .update()
                   .where(and_(fields_table.c.dir_id == dir_id,
                               fields_table.c.fieldname == fieldname))
                   .values(value=new_value))


def downgrade():
    conn = op.get_bind()
    rows = conn.execute(sql.select([fields_table.c.dir_id,
                                    fields_table.c.fieldname,
                                    fields_table.c.value]))
    to_upgrade = {(row.dir_id, row.fieldname): row.value for row in rows}
    for (dir_id, fieldname), value in to_upgrade.items():
        new_value = value.replace('{', '').replace('}', '')
        op.execute(fields_table
                   .update()
                   .where(and_(fields_table.c.dir_id == dir_id,
                               fields_table.c.fieldname == fieldname))
                   .values(value=new_value))
