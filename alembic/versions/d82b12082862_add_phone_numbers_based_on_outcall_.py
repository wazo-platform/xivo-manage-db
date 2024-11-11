"""Add phone numbers based on outcall caller ID

Revision ID: d82b12082862
Revises: 59c0eedf8853

"""

import re

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd82b12082862'
down_revision = '59c0eedf8853'

CALLER_ID_ALL_REGEX = re.compile(r'^"(.*)" <(\+?\d{3,15})>$')
VALID_PHONE_NUMBER_RE = re.compile(r'^\+?\d{3,15}$')
MIN_NUMBER_COMPARISON_LENGTH = 9
NON_SIGNIFICANT_PREFIX_LENGTH = 3
E164_MAX_LENGHT = 15
NATIONAL_NUMBER_LENGTH = 10

dialpattern_table = sa.sql.table(
    'dialpattern',
    sa.sql.column('callerid'),
    sa.sql.column('typeid'),
    sa.sql.column('type'),
)
outcall_table = sa.sql.table(
    'outcall',
    sa.sql.column('id'),
    sa.sql.column('tenant_uuid'),
)
phone_number_table = sa.sql.table(
    'phone_number',
    sa.sql.column('number'),
    sa.sql.column('tenant_uuid'),
    sa.sql.column('shared'),
    sa.sql.column('caller_id_name'),
)
trunk_outcall_table = sa.sql.table(
    'outcalltrunk',
    sa.sql.column('trunkfeaturesid'),
    sa.sql.column('outcallid'),
    sa.sql.column('priority'),
)
trunkfeatures_table = sa.sql.table(
    'trunkfeatures',
    sa.sql.column('id'),
    sa.sql.column('outgoing_caller_id_format'),
)

def _extract_number_from_caller_id(callerid):
    '''
    Extracts phone number from caller ID
    "Foobar" <+1234567890> -> +1234567890
    1234567890 -> 1234567890
    '''
    if not callerid:
        raise ValueError('Caller ID is empty')

    if (matches := CALLER_ID_ALL_REGEX.match(callerid)):
        name = matches.group(1)
        number = matches.group(2)
    else:
        name = None
        number = callerid
    
    if VALID_PHONE_NUMBER_RE.match(number):
        return name, number
    
    raise ValueError(f'Invalid caller ID: {callerid}')

def _get_outcall_trunk_map():
    outcall_trunk_map = {}
    query = trunk_outcall_table.select().where(
        trunk_outcall_table.c.priority == 0,
    )
    trunk_outcalls = op.get_bind().execute(query)
    for trunk_outcall in trunk_outcalls:
        outcall_trunk_map[trunk_outcall.outcallid] = trunk_outcall.trunkfeaturesid
    return outcall_trunk_map

def _get_existing_phone_numbers():
    numbers = []
    query = phone_number_table.select()
    phone_numbers = op.get_bind().execute(query)
    for phone_number in phone_numbers:
        numbers.append({
            'number': phone_number.number,
            'tenant_uuid': phone_number.tenant_uuid,
        })
    return numbers

def _get_outcall_tenants():
    outcall_tenants = {}
    query = outcall_table.select()
    outcalls = op.get_bind().execute(query)
    for outcall in outcalls:
        outcall_tenants[outcall.id] = outcall.tenant_uuid
    return outcall_tenants

def _get_configured_caller_ids(outcall_tenants):
    configured_caller_ids = []
    query = dialpattern_table.select().where(
        dialpattern_table.c.type == 'outcall',
    )
    dialpatterns = op.get_bind().execute(query)
    for dialpattern in dialpatterns:
        try:
            name, number = _extract_number_from_caller_id(dialpattern.callerid)
        except ValueError:
            continue

        outcall_id = int(dialpattern.typeid)
        if outcall_id in outcall_tenants:
            configured_caller_ids.append(
                {
                    'number': number,
                    'caller_id_name': name,
                    'outcall_id': outcall_id,
                    'tenant_uuid': outcall_tenants[outcall_id],
                }
            )
    return configured_caller_ids

def _insert_phone_number(existing_numbers, configured_caller_id):
    if _number_exists(existing_numbers, configured_caller_id):
        return
    number = configured_caller_id['number']
    tenant_uuid = configured_caller_id['tenant_uuid']
    query = phone_number_table.insert().values(
        number=number,
        tenant_uuid=tenant_uuid,
        caller_id_name=configured_caller_id['caller_id_name'],
        shared=True,
    )
    op.execute(query)
    existing_numbers.append({'number': number, 'tenant_uuid': tenant_uuid})

def _update_trunk_format(outcall_id, configured_caller_id):
    query = trunkfeatures_table.update().where(
        trunkfeatures_table.c.id == outcall_id,
    ).values(
        outgoing_caller_id_format=configured_caller_id['format'],
    )
    op.execute(query)

def _is_plus_e164(number):
    if not number.startswith('+'):
        return False
    return _is_e164(number[1:])

def _is_e164(number):
    if not number.isdigit():
        return False
    if NATIONAL_NUMBER_LENGTH < len(number) <= E164_MAX_LENGHT:
        return True
    return False

def _is_national(number):
    '''
    This is a very bad implementation. It works in
    North America and France.
    '''
    if not number.isdigit():
        return False
    return len(number) <= NATIONAL_NUMBER_LENGTH

def _guess_caller_id_format(configured_caller_id):
    number = configured_caller_id['number']
    if _is_plus_e164(number):
        configured_caller_id['format'] = '+E164'
    elif _is_e164(number):
        configured_caller_id['format'] = 'E164'
    elif _is_national(number):
        configured_caller_id['format'] = 'national'
    else:
        configured_caller_id['format'] = '+E164'
    return configured_caller_id


def _lastn(number, length):
    return number[len(number) - length:]

def _number_exists(existing_numbers, configured_caller_id):
    # Checks if a number is already configured in the phone_number table
    number = configured_caller_id['number']
    tenant_uuid = configured_caller_id['tenant_uuid']

    for existing_number in existing_numbers:
        if existing_number['tenant_uuid'] != tenant_uuid:
            continue

        candidate = existing_number['number']

        # exact match
        if candidate == number:
            return True
        
        # Too short to do a partial match
        if len(candidate) < MIN_NUMBER_COMPARISON_LENGTH:
            continue

        # Partial match based on the end of the number
        length_to_compare = len(candidate) - NON_SIGNIFICANT_PREFIX_LENGTH
        if _lastn(candidate, length_to_compare) == _lastn(number, length_to_compare):
            return True

    return False


def upgrade():
    existing_numbers = _get_existing_phone_numbers()
    outcall_tenants = _get_outcall_tenants()
    configured_caller_ids = _get_configured_caller_ids(outcall_tenants)
    for configured_caller_id in configured_caller_ids:
        _guess_caller_id_format(configured_caller_id)
        if _number_exists(existing_numbers, configured_caller_id):
            continue
        _insert_phone_number(existing_numbers, configured_caller_id)
    trunk_outcall_map = _get_outcall_trunk_map()
    for outcall_id in outcall_tenants.keys():
        configured = False
        trunk_id = trunk_outcall_map.get(outcall_id)
        if not trunk_id:
            continue

        for configured_caller_id in configured_caller_ids:
            if configured:
                continue
            if configured_caller_id['outcall_id'] != outcall_id:
                continue
            _update_trunk_format(trunk_id, configured_caller_id)
            configured = True


def downgrade():
    return
