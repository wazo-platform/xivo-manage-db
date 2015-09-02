"""voicemail_extra_options

Revision ID: 41f6ef3f00fe
Revises: 444b39e9aa32

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy import sql, Column, String, Integer, Enum, Text, Float
from sqlalchemy.dialects.postgresql import ARRAY

# revision identifiers, used by Alembic.
revision = '41f6ef3f00fe'
down_revision = '444b39e9aa32'


OPTIONS = ('dialout',
           'callback',
           'exitcontext',
           'saycid',
           'review',
           'operator',
           'envelope',
           'sayduration',
           'saydurationm',
           'sendvoicemail',
           'forcename',
           'forcegreetings',
           'hidefromdir',
           'emailsubject',
           'emailbody',
           'imapuser',
           'imappassword',
           'imapfolder',
           'imapvmsharedid',
           'attachfmt',
           'serveremail',
           'locale',
           'tempgreetwarn',
           'messagewrap',
           'moveheard',
           'minsecs',
           'maxsecs',
           'nextaftercmd',
           'backupdeleted',
           'volgain',
           'passwordlocation')


NUMERIC_OPTIONS = ('minsecs',
                   'maxsecs',
                   'backupdeleted',
                   'volgain')


LEGACY_FLAGS = ('saycid',
                'review',
                'operator',
                'envelope',
                'sayduration',
                'saydurationm',
                'forcename',
                'forcegreetings',
                'tempgreetwarn',
                'messagewrap',
                'moveheard',
                'nextaftercmd',
                'backupdeleted')


def gen_columns():
    return (Column('dialout', String(39)),
            Column('callback', String(39)),
            Column('exitcontext', String(39)),
            Column('saycid', Integer),
            Column('review', Integer),
            Column('operator', Integer),
            Column('envelope', Integer),
            Column('sayduration', Integer),
            Column('saydurationm', Integer),
            Column('sendvoicemail', Integer),
            Column('forcename', Integer),
            Column('forcegreetings', Integer),
            Column('hidefromdir',
                   Enum('no', 'yes', name='voicemail_hidefromdir'),
                   nullable=False,
                   server_default='no'),
            Column('emailsubject', String(1024)),
            Column('emailbody', Text),
            Column('imapuser', String(1024)),
            Column('imappassword', String(1024)),
            Column('imapfolder', String(1024)),
            Column('imapvmsharedid', String(1024)),
            Column('attachfmt', String(1024)),
            Column('serveremail', String(1024)),
            Column('locale', String(1024)),
            Column('tempgreetwarn', Integer),
            Column('messagewrap', Integer),
            Column('moveheard', Integer),
            Column('minsecs', Integer),
            Column('maxsecs', Integer),
            Column('nextaftercmd', Integer),
            Column('backupdeleted', Integer),
            Column('volgain', Float),
            Column('passwordlocation',
                   Enum('spooldir', 'voicemail', name='voicemail_passwordlocation')),
            )


def upgrade():
    op.add_column('voicemail', sa.Column('options',
                                         ARRAY(sa.String, dimensions=2),
                                         nullable=False, server_default='{}'))

    voicemail = sql.table('voicemail',
                          sql.column('uniqueid'),
                          sql.column('options'),
                          *gen_columns())

    query = sql.select([voicemail])

    for row in op.get_bind().execute(query):
        op.execute(
            voicemail
            .update()
            .values(options=convert_options(row))
            .where(voicemail.c.uniqueid == row.uniqueid)
        )

    for name in OPTIONS:
        op.drop_column('voicemail', name)
    for enum in ('voicemail_hidefromdir', 'voicemail_passwordlocation'):
        op.execute("DROP TYPE IF EXISTS {}".format(enum))


def convert_options(row):
    options = []
    for name in OPTIONS:
        value = getattr(row, name)
        if value:
            options.append(convert_option(name, value))
    return options


def convert_option(name, value):
    if isinstance(value, (int, float)):
        if name in NUMERIC_OPTIONS:
            value = str(value)
        else:
            value = "yes" if value == 1 else "no"

    value = (value
             .replace("\n", "\\n")
             .replace("\r", "\\r")
             .replace("\t", "\\t")
             .replace("|", ""))

    return [name, value]


def downgrade():
    for column in gen_columns():
        op.add_column('voicemail', column)

    voicemail = sql.table('voicemail',
                          sql.column('uniqueid'),
                          sql.column('options'),
                          *gen_columns())

    query = sql.select([voicemail.c.uniqueid, voicemail.c.options])

    for row in op.get_bind().execute(query):
        op.execute(
            voicemail
            .update()
            .values(**convert_legacy(row))
            .where(voicemail.c.uniqueid == row.uniqueid)
        )

    op.drop_column('voicemail', 'options')


def convert_legacy(row):
    values = {}
    for name, value in row.options:
        if name == 'volgain':
            value = float(value)
        elif name in NUMERIC_OPTIONS:
            value = int(value)
        elif name in LEGACY_FLAGS:
            value = int(value == "yes")
        values[name] = value
    return values
