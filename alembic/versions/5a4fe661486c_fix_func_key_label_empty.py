"""fix_func_key_label_empty

Revision ID: 5a4fe661486c
Revises: 43c5188319dc

"""

from alembic import op
from sqlalchemy import sql

# revision identifiers, used by Alembic.
revision = '5a4fe661486c'
down_revision = '43c5188319dc'


func_key_mapping = sql.table('func_key_mapping',
                             sql.column('label'))


def upgrade():
    query = (func_key_mapping
             .update()
             .values(label=None)
             .where(sql.func.trim(func_key_mapping.c.label) == '')
             )

    op.execute(query)


def downgrade():
    query = (func_key_mapping
             .update()
             .values(label='')
             .where(func_key_mapping.c.label == None)
             )

    op.execute(query)
