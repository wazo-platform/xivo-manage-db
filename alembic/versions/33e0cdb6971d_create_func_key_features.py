"""create func key features

Revision ID: 33e0cdb6971d
Revises: 4c13318f6975
XiVO Version: <version>

"""

# revision identifiers, used by Alembic.
revision = '33e0cdb6971d'
down_revision = '4c13318f6975'

from alembic import op
import sqlalchemy as sa


TRANSFER_TYPE_NAME = 'transfer'

FEATURES_DESTINATION_ID = 8
FEATURES_DESTINATION_NAME = 'features'


func_key_table = sa.sql.table('func_key',
                              sa.sql.column('id'),
                              sa.sql.column('type_id'),
                              sa.sql.column('destination_type_id'))

func_key_type_table = sa.sql.table('func_key_type',
                                   sa.sql.column('id'),
                                   sa.sql.column('name'))

func_key_destination_type_table = sa.sql.table('func_key_destination_type',
                                               sa.sql.column('id'),
                                               sa.sql.column('name'))

func_key_dest_features_table = sa.sql.table('func_key_dest_features',
                                            sa.sql.column('func_key_id'),
                                            sa.sql.column('destination_type_id'),
                                            sa.sql.column('features_id'))


def upgrade():
    type_id = insert_transfer_type()
    destination_type_id = insert_features_destination_type()
    create_dest_features_table()
    insert_parking_func_key(type_id, destination_type_id)


def insert_transfer_type():
    query = (func_key_type_table
             .insert()
             .returning(func_key_type_table.c.id)
             .values(name=TRANSFER_TYPE_NAME))

    return op.get_bind().execute(query).scalar()


def insert_features_destination_type():
    query = (func_key_destination_type_table
             .insert()
             .returning(func_key_destination_type_table.c.id)
             .values(id=FEATURES_DESTINATION_ID,
                     name=FEATURES_DESTINATION_NAME))

    return op.get_bind().execute(query).scalar()


def create_dest_features_table():
    op.create_table(
        'func_key_dest_features',
        sa.Column('func_key_id', sa.Integer),
        sa.Column('destination_type_id',
                  sa.Integer,
                  sa.CheckConstraint('destination_type_id = %d' % FEATURES_DESTINATION_ID),
                  server_default=str(FEATURES_DESTINATION_ID)),
        sa.Column('features_id', sa.Integer),
        sa.PrimaryKeyConstraint('func_key_id', 'destination_type_id'),
        sa.ForeignKeyConstraint(['func_key_id', 'destination_type_id'],
                                ['func_key.id', 'func_key.destination_type_id']),
        sa.ForeignKeyConstraint(['features_id'], ['features.id'])
    )


def insert_parking_func_key(type_id, destination_type_id):
    query = (func_key_table
             .insert()
             .returning(func_key_table.c.id)
             .values(type_id=type_id,
                     destination_type_id=destination_type_id))

    return op.get_bind().execute(query).scalar()


def downgrade():
    op.execute(func_key_dest_features_table.delete())

    op.execute(func_key_table
               .delete()
               .where(func_key_table.c.destination_type_id == FEATURES_DESTINATION_ID))

    op.execute(func_key_destination_type_table
               .delete()
               .where(func_key_destination_type_table.c.id == FEATURES_DESTINATION_ID))

    op.execute(func_key_type_table
               .delete()
               .where(func_key_type_table.c.name == TRANSFER_TYPE_NAME))

    op.drop_table('func_key_dest_features')
