"""add-parking-function-key

Revision ID: b65364a583d8
Revises: 9938e92f8be0

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'b65364a583d8'
down_revision = '9938e92f8be0'

DESTINATION_ID = 14
DESTINATION_NAME = 'parking'
func_key_destination_type_table = sa.sql.table(
    'func_key_destination_type',
    sa.sql.column('id'),
    sa.sql.column('name'),
)


def upgrade():
    insert_query = func_key_destination_type_table.insert().values(
        id=DESTINATION_ID,
        name=DESTINATION_NAME,
    )
    op.get_bind().execute(insert_query)

    op.create_table(
        'func_key_dest_parking',
        sa.Column('func_key_id', sa.Integer),
        sa.Column(
            'destination_type_id',
            sa.Integer,
            sa.CheckConstraint('destination_type_id = %d' % DESTINATION_ID),
            server_default=str(DESTINATION_ID),
        ),
        sa.Column(
            'parking_lot_id',
            sa.Integer,
            sa.ForeignKey('parking_lot.id'),
            nullable=False,
            unique=True,
        ),
        sa.PrimaryKeyConstraint('func_key_id', 'destination_type_id'),
        sa.ForeignKeyConstraint(
            ['func_key_id', 'destination_type_id'],
            ['func_key.id', 'func_key.destination_type_id'],
        ),
    )


def downgrade():
    query = (
        func_key_destination_type_table
        .delete()
        .where(func_key_destination_type_table.c.id == DESTINATION_ID)
    )
    op.get_bind().execute(query)

    op.drop_table('func_key_dest_parking')
