"""add_unique_constraint_to_user_email

Revision ID: 4fe888586ba3
Revises: 3420040c5650

"""

# revision identifiers, used by Alembic.
revision = '4fe888586ba3'
down_revision = '3420040c5650'

from alembic import op
import sqlalchemy as sa
from sqlalchemy import sql


userfeatures_table = sql.table('userfeatures',
                               sql.column('id'),
                               sql.column('email'))


def upgrade():
    _delete_duplicate_emails()
    op.create_unique_constraint('userfeatures_email', 'userfeatures', ['email'])


def _delete_duplicate_emails():
    for duplicate in _get_duplicate_emails():
        print('[MIGRATE_USER_EMAIL] : Deleting email "{}" for user id "{}"'.format(
            duplicate.email, duplicate.array_id
        ))
        query = (userfeatures_table.update()
                                   .values(email=None)
                                   .where(userfeatures_table.c.email == duplicate.email))
        op.get_bind().execute(query)


def _get_duplicate_emails():
    query = (sql.select([userfeatures_table.c.email,
                         sa.func.array_agg(userfeatures_table.c.id).label('array_id')])
                .group_by(userfeatures_table.c.email)
                .having(sa.func.count(userfeatures_table.c.email) > 1))

    return op.get_bind().execute(query)


def downgrade():
    op.drop_constraint('userfeatures_email', 'userfeatures')
