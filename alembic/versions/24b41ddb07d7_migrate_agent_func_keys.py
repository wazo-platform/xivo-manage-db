"""migrate agent func keys

Revision ID: 24b41ddb07d7
Revises: 13917b00e63c

"""

# revision identifiers, used by Alembic.
revision = '24b41ddb07d7'
down_revision = '13917b00e63c'

from alembic import op
import sqlalchemy as sa
from sqlalchemy import sql


TYPE_ID = 1
DESTINATION_TYPE_ID = 11

ACTIONS = {'agentstaticlogtoggle': 'toggle',
           'agentstaticlogin': 'login',
           'agentstaticlogoff': 'logoff'}

AGENT_TYPES = ('agentstaticlogtoggle', 'agentstaticlogin', 'agentstaticlogoff')

phonefunckey_table = sql.table('phonefunckey',
                               sql.column('iduserfeatures'),
                               sql.column('fknum'),
                               sql.column('exten'),
                               sql.column('typeextenumbers'),
                               sql.column('typevalextenumbers'),
                               sql.column('typeextenumbersright'),
                               sql.column('typevalextenumbersright'),
                               sql.column('label'),
                               sql.column('supervision'),
                               sql.column('progfunckey'))

func_key_table = sql.table('func_key',
                           sql.column('id'),
                           sql.column('type_id'),
                           sql.column('destination_type_id'))

dest_agent_table = sql.table('func_key_dest_agent',
                             sql.column('func_key_id'),
                             sql.column('destination_type_id'),
                             sql.column('agent_id'),
                             sql.column('action'))

func_key_type_table = sql.table('func_key_type',
                                sql.column('id'),
                                sql.column('name'))

func_key_mapping_table = sql.table('func_key_mapping',
                                   sql.column('template_id'),
                                   sql.column('func_key_id'),
                                   sql.column('destination_type_id'),
                                   sql.column('label'),
                                   sql.column('position'),
                                   sql.column('blf'))

template_table = sql.table('func_key_template', sql.column('id'))

user_table = sql.table('userfeatures',
                       sql.column('id'),
                       sql.column('func_key_private_template_id'))

destination_type_table = sql.table('func_key_destination_type',
                                   sql.column('id'),
                                   sql.column('name'))

agent_table = sql.table('agentfeatures',
                        sql.column('id'))


def upgrade():
    delete_missing_agents()
    delete_duplicate_agents()
    create_agent_func_keys()
    migrate_func_keys()
    delete_old_func_keys()


def create_agent_func_keys():
    agent_query = sql.select([agent_table.c.id])
    rows = op.get_bind().execute(agent_query)

    for row in rows:
        for action in ACTIONS.values():
            create_agent_func_key(row.id, action)


def delete_duplicate_agents():
    for row in get_duplicate_agents():
        delete_duplicate_fk(row.iduserfeatures, row.fknum)


def get_duplicate_agents():
    columns = (phonefunckey_table.c.iduserfeatures,
               phonefunckey_table.c.typevalextenumbers,
               sa.func.min(phonefunckey_table.c.fknum).label("first_position"))

    duplicate_query = (sql.select(columns)
                       .where(
                           phonefunckey_table.c.typevalextenumbers.in_(AGENT_TYPES))
                       .group_by(
                           phonefunckey_table.c.typevalextenumbers,
                           phonefunckey_table.c.iduserfeatures)
                       .having(
                           sa.func.count(phonefunckey_table.c.typevalextenumbers) > 1)
                       .alias())

    columns = (phonefunckey_table.c.iduserfeatures,
               phonefunckey_table.c.fknum)

    join_condition = phonefunckey_table.join(
        duplicate_query,
        sql.and_(
            phonefunckey_table.c.typevalextenumbers == duplicate_query.c.typevalextenumbers,
            phonefunckey_table.c.fknum > duplicate_query.c.first_position,
            phonefunckey_table.c.iduserfeatures == duplicate_query.c.iduserfeatures))

    duplicate_fk_query = sql.select(columns, from_obj=[join_condition])

    return op.get_bind().execute(duplicate_fk_query)


def delete_duplicate_fk(iduserfeatures, fknum):
    print('[MIGRATE_FK] : Deleting duplicate agent func key for user "%s" (fk position %s)' %
          (iduserfeatures, fknum))

    query = (phonefunckey_table
             .delete()
             .where(sql.and_(
                 phonefunckey_table.c.iduserfeatures == iduserfeatures,
                 phonefunckey_table.c.fknum == fknum)))

    op.get_bind().execute(query)


def delete_missing_agents():
    agent_query = sql.select([agent_table.c.id])

    query = (phonefunckey_table
             .delete()
             .where(
                 sql.and_(
                     phonefunckey_table.c.typevalextenumbers.in_(AGENT_TYPES),
                     sql.cast(phonefunckey_table.c.typevalextenumbersright, sa.Integer)
                        .notin_(agent_query)))
             )

    op.get_bind().execute(query)


def migrate_func_keys():
    for row in get_func_keys():
        func_key_id = find_agent_func_key_id(row.agent_id, row.action)
        create_mapping(func_key_id, row)


def get_func_keys():
    columns = (
        phonefunckey_table.c.iduserfeatures.label('user_id'),
        phonefunckey_table.c.fknum.label('position'),
        phonefunckey_table.c.label,
        phonefunckey_table.c.typevalextenumbers.label('action'),
        sql.cast(phonefunckey_table.c.typevalextenumbersright, sa.Integer).label('agent_id'),
        sql.cast(phonefunckey_table.c.supervision, sa.Boolean).label('blf'),
    )

    query = (sql.select(columns)
             .where(
                 phonefunckey_table.c.typevalextenumbers.in_(AGENT_TYPES))
             )

    return op.get_bind().execute(query)


def find_agent_func_key_id(agent_id, action):
    query = (sql.select([dest_agent_table.c.func_key_id])
             .where(
                 sql.and_(
                     dest_agent_table.c.agent_id == agent_id,
                     dest_agent_table.c.action == ACTIONS[action]))
             )

    return op.get_bind().execute(query).scalar()


def create_agent_func_key(agent_id, action):
    func_key_query = (func_key_table
                      .insert()
                      .returning(func_key_table.c.id)
                      .values(type_id=TYPE_ID,
                              destination_type_id=DESTINATION_TYPE_ID)
                      )

    func_key_id = op.get_bind().execute(func_key_query).scalar()

    agent_query = (dest_agent_table
                   .insert()
                   .returning(dest_agent_table.c.func_key_id)
                   .values(func_key_id=func_key_id,
                           destination_type_id=DESTINATION_TYPE_ID,
                           agent_id=agent_id,
                           action=action)
                   )

    op.get_bind().execute(agent_query)

    return func_key_id


def create_mapping(func_key_id, func_key_row):
    conn = op.get_bind()

    template_query = (
        sql.select(
            [user_table.c.func_key_private_template_id])
        .where(
            user_table.c.id == func_key_row.user_id))

    template_id = conn.execute(template_query).scalar()

    mapping_query = (func_key_mapping_table
                     .insert()
                     .returning(func_key_mapping_table.c.func_key_id)
                     .values(func_key_id=func_key_id,
                             template_id=template_id,
                             destination_type_id=DESTINATION_TYPE_ID,
                             label=func_key_row.label,
                             position=func_key_row.position,
                             blf=func_key_row.blf))

    conn.execute(mapping_query)


def delete_old_func_keys():
    delete_query = (phonefunckey_table
                    .delete()
                    .where(
                        phonefunckey_table.c.typevalextenumbers.in_(AGENT_TYPES))
                    )

    op.get_bind().execute(delete_query)


def downgrade():
    for row in get_old_func_keys():
        create_old_func_keys(row)
        delete_mapping(row.func_key_id, row.template_id)


def get_old_func_keys():
    columns = (
        func_key_mapping_table.c.func_key_id,
        func_key_mapping_table.c.template_id,
        func_key_mapping_table.c.position,
        func_key_mapping_table.c.blf,
        func_key_mapping_table.c.label,
        dest_agent_table.c.agent_id,
        dest_agent_table.c.action,
        user_table.c.id.label('user_id')
    )

    join_conditions = (func_key_mapping_table
                       .join(dest_agent_table,
                             func_key_mapping_table.c.func_key_id == dest_agent_table.c.func_key_id)
                       .join(template_table,
                             func_key_mapping_table.c.template_id == template_table.c.id)
                       .join(user_table,
                             template_table.c.id == user_table.c.func_key_private_template_id))

    query = (sql.select(columns, from_obj=[join_conditions]))

    return op.get_bind().execute(query)


def create_old_func_keys(row):
    supervision = 1 if row.blf else 0
    reversed_actions = {value: key for key, value in ACTIONS.iteritems()}

    row = {'iduserfeatures': row.user_id,
           'fknum': row.position,
           'typeextenumbers': 'extenfeatures',
           'typevalextenumbers': reversed_actions[row.action],
           'typeextenumbersright': 'agent',
           'typevalextenumbersright': row.agent_id,
           'label': row.label,
           'exten': None,
           'supervision': supervision}

    op.bulk_insert(phonefunckey_table, [row])


def delete_mapping(func_key_id, template_id):
    query = (func_key_mapping_table
             .delete()
             .where(sql.and_(
                 func_key_mapping_table.c.func_key_id == func_key_id,
                 func_key_mapping_table.c.template_id == template_id)))

    op.get_bind().execute(query)
