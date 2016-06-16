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
                            sql.column('presence_id'),
                            sql.column('name'),
                            sql.column('display_name'),
                            sql.column('actions'),
                            sql.column('color'),
                            sql.column('access_status'),
                            sql.column('deletable'))
old, new = 'xivo', 'francais'
english_params = ['english', 'Default english presence statuses']

available = ['available', 'Available', 'enablednd(false)', '#9BC920', '1,2,3,4,5', 0]
away = ['away', 'Away', 'enablednd(false)', '#FFDD00', '1,2,3,4,5', 1]
outtolunch = ['outtolunch', 'Out to lunch', 'enablednd(false)', '#6CA6FF', '1,2,3,4,5', 1]
dnd = ['donotdisturb', 'Do not disturb', 'enablednd(true)', '#D13224', '1,2,3,4,5', 1]
brb = ['berightback', 'Be right back', 'enablednd(false)', '#F2833A', '1,2,3,4,5', 1]
disconnected = ['disconnected', 'Disconnected', 'agentlogoff()', '#9E9E9E', '', 0]
english_presences = [
    available,
    away,
    outtolunch,
    dnd,
    brb,
    disconnected,
]


def rename_presences(old, new):
    op.execute(ctipresences_table.update().where(ctipresences_table.c.name == old).values(name=new))


def add_presences(name, description):
    conn = op.get_bind()
    op.execute(ctipresences_table.insert().values(name=name,
                                                  description=description,
                                                  deletable=0))
    id_ = 0
    for row in conn.execute(ctipresences_table.select()):
        id_ = row['id'] if row['id'] > id_ else id_

    return id_


def remove_presences(name, description):
    op.execute(ctipresences_table.delete().where(and_(ctipresences_table.c.name == name,
                                                      ctipresences_table.c.description == description,
                                                      ctipresences_table.c.deletable == 0)))


def insert_english_presences(presence_id, presences):
    for name, display_name, actions, color, access_status, deletable in presences:
        op.execute(ctistatus_table.insert().values(
            presence_id=presence_id,
            name=name,
            display_name=display_name,
            actions=actions,
            color=color,
            access_status=access_status,
            deletable=deletable,
        ))


def upgrade():
    rename_presences(old, new)
    presence_id = add_presences(*english_params)
    insert_english_presences(presence_id, english_presences)


def downgrade():
    remove_presences(*english_params)
    rename_presences(new, old)
