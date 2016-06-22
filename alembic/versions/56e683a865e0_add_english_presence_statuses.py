"""add english presence statuses

Revision ID: 56e683a865e0
Revises: da58e9e49eb

"""

# revision identifiers, used by Alembic.
revision = '56e683a865e0'
down_revision = 'da58e9e49eb'

from alembic import op
from sqlalchemy import and_, sql

ctipresences_table = sql.table('ctipresences',
                               sql.column('id'),
                               sql.column('name'),
                               sql.column('description'),
                               sql.column('deletable'))
ctistatus_table = sql.table('ctistatus',
                            sql.column('id'),
                            sql.column('presence_id'),
                            sql.column('name'),
                            sql.column('display_name'),
                            sql.column('actions'),
                            sql.column('color'),
                            sql.column('access_status'),
                            sql.column('deletable'))
old, new = 'xivo', 'francais'
english_params = ['english', 'Default english presence statuses']

available = ['available', 'Available', 'enablednd(false)', '#9BC920', 0]
away = ['away', 'Away', 'enablednd(false)', '#FFDD00', 1]
outtolunch = ['outtolunch', 'Out to lunch', 'enablednd(false)', '#6CA6FF', 1]
dnd = ['donotdisturb', 'Do not disturb', 'enablednd(true)', '#D13224', 1]
brb = ['berightback', 'Be right back', 'enablednd(false)', '#F2833A', 1]
disconnected = ['disconnected', 'Disconnected', 'agentlogoff()', '#9E9E9E', 0]
english_presences = [
    available,
    away,
    outtolunch,
    dnd,
    brb,
    disconnected,
]
available_presence_map = {
    'available': ['available', 'away', 'outtolunch', 'donotdisturb', 'berightback'],
    'away': ['available', 'away', 'outtolunch', 'donotdisturb', 'berightback'],
    'outtolunch': ['available', 'away', 'outtolunch', 'donotdisturb', 'berightback'],
    'donotdisturb': ['available', 'away', 'outtolunch', 'donotdisturb', 'berightback'],
    'berightback': ['available', 'away', 'outtolunch', 'donotdisturb', 'berightback'],
    'disconnected': [],
}


def rename_presences(old, new):
    op.execute(ctipresences_table.update().where(ctipresences_table.c.name == old).values(name=new))


def add_presence_group(name, description):
    insert_query = (ctipresences_table
                    .insert()
                    .returning(ctipresences_table.c.id)
                    .values(name=name,
                            description=description,
                            deletable=0))
    return op.get_bind().execute(insert_query).scalar()


def remove_presences(name, description):
    op.execute(ctipresences_table.delete().where(and_(ctipresences_table.c.name == name,
                                                      ctipresences_table.c.description == description,
                                                      ctipresences_table.c.deletable == 0)))


def insert_presence(group_id, name, display_name, actions, color, deletable):
    insert_query = (ctistatus_table
                    .insert()
                    .returning(ctistatus_table.c.id)
                    .values(presence_id=group_id,
                            name=name,
                            display_name=display_name,
                            actions=actions,
                            color=color,
                            deletable=deletable))
    return op.get_bind().execute(insert_query).scalar(), name


def update_presence(presence_id, avail_ids):
    op.execute(ctistatus_table
               .update()
               .where(ctistatus_table.c.id == presence_id)
               .values(access_status=avail_ids))


def insert_english_presences(group_id, presences):
    presence_map = {}
    for presence in presences:
        id_, name = insert_presence(group_id, *presence)
        presence_map[name] = id_

    for name, availability in available_presence_map.iteritems():
        presence_id = presence_map[name]
        avail_ids = ','.join([str(presence_map[avail_name]) for avail_name in availability])
        update_presence(presence_id, avail_ids)


def upgrade():
    rename_presences(old, new)
    group_id = add_presence_group(*english_params)
    insert_english_presences(group_id, english_presences)


def downgrade():
    remove_presences(*english_params)
    rename_presences(new, old)
