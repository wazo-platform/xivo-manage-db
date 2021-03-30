"""add zonemessages

Revision ID: 0f4a7c48613c
Revises: e6c5e0410e89

"""

import sqlalchemy as sa

from alembic import op
from pytz import country_timezones


# revision identifiers, used by Alembic.
revision = '0f4a7c48613c'
down_revision = 'e6c5e0410e89'

staticvoicemail_tbl = sa.table(
    'staticvoicemail',
    sa.column('commented'),
    sa.column('filename'),
    sa.column('category'),
    sa.column('var_name'),
    sa.column('var_val'),
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
            zone_format = f"{timezone}|''vm-received'' q ''digits/at'' IMp"
            yield {'name': zone_name, 'format': zone_format}


def upgrade():
    for zone in get_zones():
        query = staticvoicemail_tbl.insert().values(
            commented=0,
            filename='voicemail.conf',
            category='zonemessages',
            var_name=zone['name'],
            var_val=zone['format'],
        )
        op.get_bind().execute(query)


def downgrade():
    pass
