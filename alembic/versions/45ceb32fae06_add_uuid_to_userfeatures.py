"""add uuid to userfeatures

Revision ID: 45ceb32fae06
Revises: 2956eaa19c7c

"""

# revision identifiers, used by Alembic.
revision = '45ceb32fae06'
down_revision = '2956eaa19c7c'

import uuid

from alembic import op
import sqlalchemy as sa


def upgrade():
    # Create the column
    op.add_column('userfeatures', sa.Column('uuid', sa.String(38)))

    # Insert some initial values
    conn = op.get_bind()
    user_table = sa.sql.table('userfeatures', sa.sql.column('id'), sa.sql.column('uuid'))
    rows = conn.execute('SELECT "id" FROM "userfeatures"')
    for row in rows.fetchall():
        user_id = row[0]
        user_uuid = str(uuid.uuid4())
        op.execute(user_table.update().where(user_table.c.id == user_id).values({'uuid': user_uuid}))

    # Add the not null constraint
    op.alter_column('userfeatures', 'uuid', nullable=False)
    op.create_index('userfeatures__idx__uuid', 'userfeatures', ['uuid'])


def downgrade():
    op.drop_column('userfeatures', 'uuid')
