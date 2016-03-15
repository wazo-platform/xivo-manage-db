"""remove_cel_fields_limits

Revision ID: 3c72c43e39fa
Revises: 4fe888586ba3

"""

# revision identifiers, used by Alembic.
revision = '3c72c43e39fa'
down_revision = '4fe888586ba3'

from alembic import op
from sqlalchemy.types import String, Text, UnicodeText


def upgrade():
    op.alter_column('cel', 'eventtype', type_=Text)
    op.alter_column('cel', 'userdeftype', type_=Text)
    op.alter_column('cel', 'cid_name', type_=UnicodeText)
    op.alter_column('cel', 'cid_num', type_=UnicodeText)
    op.alter_column('cel', 'cid_ani', type_=Text)
    op.alter_column('cel', 'cid_rdnis', type_=Text)
    op.alter_column('cel', 'cid_dnid', type_=Text)
    op.alter_column('cel', 'exten', type_=UnicodeText)
    op.alter_column('cel', 'context', type_=Text)
    op.alter_column('cel', 'channame', type_=UnicodeText)
    op.alter_column('cel', 'appname', type_=Text)
    op.alter_column('cel', 'appdata', type_=Text)
    op.alter_column('cel', 'accountcode', type_=Text)
    op.alter_column('cel', 'peeraccount', type_=Text)
    op.alter_column('cel', 'uniqueid', type_=Text)
    op.alter_column('cel', 'linkedid', type_=Text)
    op.alter_column('cel', 'userfield', type_=Text)
    op.alter_column('cel', 'peer', type_=Text)


def downgrade():
    op.alter_column('cel', 'eventtype', type_=String(30))
    op.alter_column('cel', 'userdeftype', type_=String(255))
    op.alter_column('cel', 'cid_name', type_=String(80, convert_unicode=True))
    op.alter_column('cel', 'cid_num', type_=String(80, convert_unicode=True))
    op.alter_column('cel', 'cid_ani', type_=String(80))
    op.alter_column('cel', 'cid_rdnis', type_=String(80))
    op.alter_column('cel', 'cid_dnid', type_=String(80))
    op.alter_column('cel', 'exten', type_=String(80, convert_unicode=True))
    op.alter_column('cel', 'context', type_=String(80))
    op.alter_column('cel', 'channame', type_=String(80, convert_unicode=True))
    op.alter_column('cel', 'appname', type_=String(80))
    op.alter_column('cel', 'appdata', type_=String(512))
    op.alter_column('cel', 'accountcode', type_=String(20))
    op.alter_column('cel', 'peeraccount', type_=String(20))
    op.alter_column('cel', 'uniqueid', type_=String(150))
    op.alter_column('cel', 'linkedid', type_=String(150))
    op.alter_column('cel', 'userfield', type_=String(255))
    op.alter_column('cel', 'peer', type_=String(80))
