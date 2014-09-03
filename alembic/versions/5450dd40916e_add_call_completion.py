"""add call completion

Revision ID: 5450dd40916e
Revises: 2c6c9833d839
XiVO Version: 14.17

"""

# revision identifiers, used by Alembic.
revision = '5450dd40916e'
down_revision = '2c6c9833d839'

from alembic import op
import sqlalchemy as sa


extensions_table = sa.sql.table(
    'extensions',
    sa.sql.column('commented'),
    sa.sql.column('context'),
    sa.sql.column('exten'),
    sa.sql.column('type'),
    sa.sql.column('typeval'),
)


def upgrade():
    _insert_cc_extension()


def _insert_cc_extension():
    connection = op.get_bind()
    qry = 'SELECT exten, context FROM extensions WHERE context=\'xivo-features\' and exten=\'*40\''
    res = connection.execute(qry).fetchall()
    if res:
        exten = 'cctoggle'
    else:
        exten = '*40'

    op.bulk_insert(extensions_table, [{'commented': 1,
                                       'context': 'xivo-features',
                                       'exten': exten,
                                       'type': 'extenfeatures',
                                       'typeval': 'cctoggle'}])


def downgrade():
    _delete_cc_extension()


def _delete_cc_extension():
    op.execute(extensions_table
               .delete()
               .where(sa.sql.and_(
                   extensions_table.c.type == 'extenfeatures',
                   extensions_table.c.typeval == 'cctoggle',
               )))
