"""add zonemessages

Revision ID: 0f4a7c48613c
Revises: e6c5e0410e89

"""

from alembic import op
from pytz import country_timezones
from sqlalchemy import sql


# revision identifiers, used by Alembic.
revision = '0f4a7c48613c'
down_revision = 'e6c5e0410e89'

staticvoicemail_tbl = sql.table(
    'staticvoicemail',
    sql.column('cat_metric'),
    sql.column('commented'),
    sql.column('filename'),
    sql.column('category'),
    sql.column('var_name'),
    sql.column('var_val'),
)

SUPPORTED_COUNTRIES = (
    'BE',  # Belgium
    'IT',  # Italy
    'CA',  # Canada
    'DE',  # Germany
    'FR',  # France
    'IL',  # Israel
    'LU',  # Luxembourg
    'MY',  # Malaysia
    'MC',  # Monaco
    'NL',  # Netherlands
    'PL',  # Poland
    'PT',  # Portugal
    'GB',  # Britain (United Kingdom)
    'US',  # America
    'ES',  # Spain
    'CH',  # Switzerland
)


def _timezone_name(timezone_name):
    tz_name = timezone_name.split('/')
    return "-".join(tz_name[1:]).lower()


def get_zones():
    for country_code in SUPPORTED_COUNTRIES:
        timezones = country_timezones.get(country_code, [])
        for timezone in timezones:
            zone_name = f'{country_code}-{_timezone_name(timezone)}'.lower()
            # IMp is the AM/PM time format. We set it by default by choice.
            zone_format = f"{timezone}|'vm-received' q 'digits/at' IMp"
            yield {'name': zone_name, 'format': zone_format}


def _zonemessage_exists(zone_format):
    query = sql.select([sql.func.count(staticvoicemail_tbl.c.var_val)]).where(
        staticvoicemail_tbl.c.var_val == zone_format
    )
    return op.get_bind().execute(query).scalar() > 0


def upgrade():
    for zone in get_zones():
        if not _zonemessage_exists(zone['format']):
            query = staticvoicemail_tbl.insert().values(
                cat_metric=1,
                commented=0,
                filename='voicemail.conf',
                category='zonemessages',
                var_name=zone['name'],
                var_val=zone['format'],
            )
            op.get_bind().execute(query)


def downgrade():
    pass
