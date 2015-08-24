"""change defaut CTI colors

Revision ID: 387d650380bd
Revises: 5ace7dc40b5c

"""

# revision identifiers, used by Alembic.
revision = '387d650380bd'
down_revision = '5ace7dc40b5c'

from alembic import op
import sqlalchemy as sa


ctistatus_table = sa.sql.table('ctistatus',
                               sa.sql.column('presence_id'),
                               sa.sql.column('color'))
ctiphonehints_table = sa.sql.table('ctiphonehints',
                                   sa.sql.column('idgroup'),
                                   sa.sql.column('number'),
                                   sa.sql.column('color'))

OLD_GREEN = ('#08FD20', '#0DFF25')
OLD_YELLOW = ('#FDE50A', '#F7FF05')
OLD_BLUE = ('#001AFF', '#1B0AFF')
OLD_RED = ('#FF032D', '#FF0526', '#FF0008')
OLD_ORANGE = ('#F2833A',)
OLD_BLACK = ('#202020', '#000000', '#030303')
OLD_WHITE = ('#FFFFFF',)

NEW_GREEN = '#9BC920'
NEW_YELLOW = '#FFDD00'
NEW_BLUE = '#6CA6FF'
NEW_RED = '#D13224'
NEW_ORANGE = '#F2833A'
NEW_GREY = '#9E9E9E'


def upgrade():
    _upgrade_ctistatus(OLD_GREEN, NEW_GREEN)
    _upgrade_ctistatus(OLD_YELLOW, NEW_YELLOW)
    _upgrade_ctistatus(OLD_BLUE, NEW_BLUE)
    _upgrade_ctistatus(OLD_RED, NEW_RED)
    _upgrade_ctistatus(OLD_ORANGE, NEW_ORANGE)
    _upgrade_ctistatus(OLD_BLACK, NEW_GREY)

    _upgrade_ctiphonehints(OLD_GREEN, NEW_GREEN)
    _upgrade_ctiphonehints(OLD_YELLOW, NEW_YELLOW)
    _upgrade_ctiphonehints(OLD_BLUE, NEW_BLUE)
    _upgrade_ctiphonehints(OLD_RED, NEW_RED)
    _upgrade_ctiphonehints(OLD_BLACK, NEW_GREY)
    _upgrade_ctiphonehints(OLD_WHITE, NEW_GREY)


def downgrade():
    _upgrade_ctistatus([NEW_GREEN], OLD_GREEN[0])
    _upgrade_ctistatus([NEW_YELLOW], OLD_YELLOW[0])
    _upgrade_ctistatus([NEW_BLUE], OLD_BLUE[0])
    _upgrade_ctistatus([NEW_RED], OLD_RED[0])
    _upgrade_ctistatus([NEW_ORANGE], OLD_ORANGE[0])
    _upgrade_ctistatus([NEW_GREY], OLD_BLACK[0])

    _upgrade_ctiphonehints([NEW_GREEN], OLD_GREEN[0])
    _upgrade_ctiphonehints([NEW_YELLOW], OLD_YELLOW[0])
    _upgrade_ctiphonehints([NEW_BLUE], OLD_BLUE[0])
    _upgrade_ctiphonehints([NEW_RED], OLD_RED[0])
    _upgrade_ctiphonehints([NEW_GREY], OLD_BLACK[0])
    query = (ctiphonehints_table
             .update()
             .values(color=OLD_WHITE[0])
             .where(sa.sql.and_(ctiphonehints_table.c.idgroup == 1,
                                ctiphonehints_table.c.number == '4')))
    op.execute(query)


def _upgrade_ctistatus(old_colors, new_color):
    query = (ctistatus_table
             .update()
             .values(color=new_color)
             .where(sa.sql.and_(ctistatus_table.c.presence_id == 1,
                                ctistatus_table.c.color.in_(old_colors))))
    op.execute(query)


def _upgrade_ctiphonehints(old_colors, new_color):
    query = (ctiphonehints_table
             .update()
             .values(color=new_color)
             .where(sa.sql.and_(ctiphonehints_table.c.idgroup == 1,
                                ctiphonehints_table.c.color.in_(old_colors))))
    op.execute(query)
