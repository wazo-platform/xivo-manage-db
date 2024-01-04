"""remove ccss

Revision ID: 091acfe39b68
Revises: 054b024b3450

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '091acfe39b68'
down_revision = '054b024b3450'

feature_extension_table = sa.sql.table(
    'feature_extension',
    sa.sql.column('enabled'),
    sa.sql.column('exten'),
    sa.sql.column('feature'),
)


def _insert_cc_extension():
    connection = op.get_bind()
    qry = 'SELECT exten FROM feature_extension WHERE exten=\'*40\''
    res = connection.execute(qry).fetchall()
    if res:
        exten = 'cctoggle'
    else:
        exten = '*40'

    op.bulk_insert(feature_extension_table, [
        {
            'enabled': True,
            'exten': exten,
            'feature': 'cctoggle',
        },
    ])


def _delete_cc_extension():
    op.execute(feature_extension_table
               .delete()
               .where(sa.sql.and_(
                   feature_extension_table.c.feature == 'cctoggle',
               )))


def downgrade():
    _insert_cc_extension()


def upgrade():
    _delete_cc_extension()
