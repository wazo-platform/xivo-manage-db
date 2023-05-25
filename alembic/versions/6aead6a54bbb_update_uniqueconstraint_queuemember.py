"""update_uniqueconstraint_queuemember

Revision ID: 6aead6a54bbb
Revises: 2984e5ede175

"""

# revision identifiers, used by Alembic.
revision = '6aead6a54bbb'
down_revision = '2984e5ede175'

from alembic import op


table_name = 'queuemember'
old_columns_name = ['queue_name', 'channel', 'usertype', 'userid', 'category']
new_columns_name = ['queue_name', 'channel', 'interface', 'usertype', 'userid', 'category', 'position']
old_constraint_name = f'{table_name}_{"_".join(old_columns_name)}_key'
new_constraint_name = f'{table_name}_queue_name_channel_interface_usertype_userid_ca_key'


def upgrade():
    op.drop_constraint(old_constraint_name, table_name)
    op.create_unique_constraint(new_constraint_name, table_name, new_columns_name)


def downgrade():
    op.drop_constraint(new_constraint_name, table_name)
    op.create_unique_constraint(old_constraint_name, table_name, old_columns_name)
