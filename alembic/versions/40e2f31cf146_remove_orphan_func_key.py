"""remove_orphan_func_key

Revision ID: 40e2f31cf146
Revises: 3e185fe069be

"""

from alembic import op
from sqlalchemy import sql


# revision identifiers, used by Alembic.
revision = '40e2f31cf146'
down_revision = '3e185fe069be'

func_key = sql.table(
    'func_key',
    sql.column('id'),
    sql.column('destination_type_id'),
)

func_key_mapping = sql.table(
    'func_key_mapping',
    sql.column('func_key_id'),
)

func_key_dest_agent = sql.table(
    'func_key_dest_agent',
    sql.column('func_key_id'),
    sql.column('destination_type_id'),
)

func_key_dest_bsfilter = sql.table(
    'func_key_dest_bsfilter',
    sql.column('func_key_id'),
    sql.column('destination_type_id'),
)

func_key_dest_conference = sql.table(
    'func_key_dest_conference',
    sql.column('func_key_id'),
    sql.column('destination_type_id'),
)

func_key_dest_custom = sql.table(
    'func_key_dest_custom',
    sql.column('func_key_id'),
    sql.column('destination_type_id'),
)

func_key_dest_features = sql.table(
    'func_key_dest_features',
    sql.column('func_key_id'),
    sql.column('destination_type_id'),
)

func_key_dest_forward = sql.table(
    'func_key_dest_forward',
    sql.column('func_key_id'),
    sql.column('destination_type_id'),
)

func_key_dest_group = sql.table(
    'func_key_dest_group',
    sql.column('func_key_id'),
    sql.column('destination_type_id'),
)

func_key_dest_paging = sql.table(
    'func_key_dest_paging',
    sql.column('func_key_id'),
    sql.column('destination_type_id'),
)

func_key_dest_park_position = sql.table(
    'func_key_dest_park_position',
    sql.column('func_key_id'),
    sql.column('destination_type_id'),
)

func_key_dest_queue = sql.table(
    'func_key_dest_queue',
    sql.column('func_key_id'),
    sql.column('destination_type_id'),
)

func_key_dest_service = sql.table(
    'func_key_dest_service',
    sql.column('func_key_id'),
    sql.column('destination_type_id'),
)

func_key_dest_user = sql.table(
    'func_key_dest_user',
    sql.column('func_key_id'),
    sql.column('destination_type_id'),
)


def upgrade():
    func_key_results = op.get_bind().execute(
        sql.select([func_key.c.id])
        .select_from(
            func_key
            .outerjoin(func_key_dest_agent, func_key_dest_agent.c.func_key_id == func_key.c.id)
            .outerjoin(func_key_dest_bsfilter, func_key_dest_bsfilter.c.func_key_id == func_key.c.id)
            .outerjoin(func_key_dest_conference, func_key_dest_conference.c.func_key_id == func_key.c.id)
            .outerjoin(func_key_dest_custom, func_key_dest_custom.c.func_key_id == func_key.c.id)
            .outerjoin(func_key_dest_features, func_key_dest_features.c.func_key_id == func_key.c.id)
            .outerjoin(func_key_dest_forward, func_key_dest_forward.c.func_key_id == func_key.c.id)
            .outerjoin(func_key_dest_group, func_key_dest_group.c.func_key_id == func_key.c.id)
            .outerjoin(func_key_dest_paging, func_key_dest_paging.c.func_key_id == func_key.c.id)
            .outerjoin(func_key_dest_park_position, func_key_dest_park_position.c.func_key_id == func_key.c.id)
            .outerjoin(func_key_dest_queue, func_key_dest_queue.c.func_key_id == func_key.c.id)
            .outerjoin(func_key_dest_service, func_key_dest_service.c.func_key_id == func_key.c.id)
            .outerjoin(func_key_dest_user, func_key_dest_user.c.func_key_id == func_key.c.id)
        )
        .where(sql.and_(
            func_key_dest_agent.c.func_key_id == None,
            func_key_dest_bsfilter.c.func_key_id == None,
            func_key_dest_conference.c.func_key_id == None,
            func_key_dest_custom.c.func_key_id == None,
            func_key_dest_features.c.func_key_id == None,
            func_key_dest_forward.c.func_key_id == None,
            func_key_dest_group.c.func_key_id == None,
            func_key_dest_paging.c.func_key_id == None,
            func_key_dest_park_position.c.func_key_id == None,
            func_key_dest_queue.c.func_key_id == None,
            func_key_dest_service.c.func_key_id == None,
            func_key_dest_user.c.func_key_id == None,
        ))

    )
    func_key_ids = [func_key_result.id for func_key_result in func_key_results]

    if not func_key_ids:
        return

    op.execute(
        func_key_mapping
        .delete()
        .where(func_key_mapping.c.func_key_id.in_(func_key_ids))
    )
    op.execute(
        func_key
        .delete()
        .where(func_key.c.id.in_(func_key_ids))
    )


def downgrade():
    pass
