"""force user to entity association

Revision ID: 5073b1fa473e
Revises: 1f4cbd713979
Create Date: 2014-06-03 13:55:12.753391
XiVO Version: <version>

"""

# revision identifiers, used by Alembic.
revision = '5073b1fa473e'
down_revision = '1f4cbd713979'

from alembic import op
from sqlalchemy import sql


def upgrade():
    entity = sql.table(
        'entity',
        sql.column('id'),
    )
    user = sql.table(
        'userfeatures',
        sql.column('entityid'),
    )

    entity_id = _default_entity_id(entity)
    _sanitize_entity_ids(entity, user, entity_id)
    _add_foreign_key()


def downgrade():
    _delete_foreign_key()


def _add_foreign_key():
    op.create_foreign_key(
        name='userfeatures_entity_id_fkey',
        source='userfeatures',
        referent='entity',
        local_cols=['entityid'],
        remote_cols=['id'],
        ondelete='RESTRICT',
    )


def _delete_foreign_key():
    op.drop_constraint(
        name='userfeatures_entity_id_fkey',
        table_name='userfeatures',
        type_='foreignkey',
    )


def _default_entity_id(entity):
    query = sql.select([entity.c.id], limit=1)
    entity_id = op.get_bind().execute(query).scalar()
    return entity_id


def _sanitize_entity_ids(entity, user, entity_id):
    valid_entities = sql.select([entity.c.id])
    update_query = (
        user.update().values(entityid=entity_id)
        .where(
            sql.or_(
                user.c.entityid == None,
                sql.not_(user.c.entityid.in_(valid_entities))
            )
        )
    )
    op.get_bind().execute(update_query)
