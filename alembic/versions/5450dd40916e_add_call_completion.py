"""add call completion

Revision ID: 5450dd40916e
Revises: 2c6c9833d839
XiVO Version: 14.14

"""

# revision identifiers, used by Alembic.
revision = '5450dd40916e'
down_revision = '2c6c9833d839'

from alembic import op
import sqlalchemy as sa


call_completion_table = sa.sql.table(
    'call_completion',
)

extensions_table = sa.sql.table(
    'extensions',
    sa.sql.column('commented'),
    sa.sql.column('context'),
    sa.sql.column('exten'),
    sa.sql.column('type'),
    sa.sql.column('typeval'),
)


def upgrade():
    _create_cc_table()
    _insert_cc_extensions()


def _create_cc_table():
    op.create_table(
        'call_completion',
        sa.Column('id', sa.Integer),
        sa.Column('enabled', sa.Boolean, nullable=False, server_default='FALSE'),
        sa.Column('cc_offer_timer', sa.Integer, nullable=False, server_default='30'),
        sa.Column('ccbs_available_timer', sa.Integer, nullable=False, server_default='900'),
        sa.Column('ccnr_available_timer', sa.Integer, nullable=False, server_default='900'),
        sa.Column('cc_recall_timer', sa.Integer, nullable=False, server_default='30'),
        sa.PrimaryKeyConstraint('id'),
    )
    op.execute(call_completion_table.insert().values())


def _insert_cc_extensions():
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
    _drop_cc_table()
    _delete_cc_extensions()


def _drop_cc_table():
    op.drop_table('call_completion')


def _delete_cc_extensions():
    op.execute(extensions_table
            .delete()
            .where(sa.sql.and_(
                extensions_table.c.type == 'extenfeatures',
                extensions_table.c.typeval == 'cctoggle',
            )))
