"""migrate incall main number to phone_number

Revision ID: b8a823cde2fc
Revises: a93b2625be0d

"""

from alembic import op
import sqlalchemy as sa
import re


# revision identifiers, used by Alembic.
revision = 'b8a823cde2fc'
down_revision = 'a93b2625be0d'

VALID_PHONE_NUMBER_RE = re.compile(r'^\+?\d{3,15}$')
MIN_NUMBER_COMPARISON_LENGTH = 9
NON_SIGNIFICANT_PREFIX_LENGTH = 3


incall_table = sa.sql.table(
    'incall',
    sa.sql.column('id'),
    sa.sql.column('tenant_uuid'),
    sa.sql.column('main'),
)
extensions_table = sa.sql.table(
    'extensions',
    sa.sql.column('id'),
    sa.sql.column('type'),
    sa.sql.column('typeval'),
    sa.sql.column('context'),
    sa.sql.column('exten'),
)
phone_number_table = sa.sql.table(
    'phone_number',
    sa.sql.column('number'),
    sa.sql.column('tenant_uuid'),
    sa.sql.column('shared'),
    sa.sql.column('caller_id_name'),
    sa.sql.column('main'),
)


def _get_existing_phone_numbers():
    numbers = []
    query = phone_number_table.select()
    phone_numbers = op.get_bind().execute(query)
    for phone_number in phone_numbers:
        numbers.append({
            'number': phone_number.number,
            'tenant_uuid': phone_number.tenant_uuid,
            'main': phone_number.main
        })
    return numbers


def _get_incall_main_number_by_tenant():
    query = incall_table.join(
        extensions_table,
        onclause=sa.and_(
            extensions_table.c.type == 'incall',
            incall_table.c.id == sa.cast(extensions_table.c.typeval, sa.Integer),
        )
    ).select().where(
        incall_table.c.main
    )
    incalls = op.get_bind().execute(query)
    incall_by_tenants = {
        incall['tenant_uuid']: incall
        for incall in incalls
    }
    return incall_by_tenants


def _insert_main_phone_numbers(existing_numbers, new_numbers):
    # NOTE: we don't override an existing main number in tenant
    actually_new_numbers = [
        number
        for number in new_numbers
        if not _number_exists(existing_numbers, number)
        and not any(
            existing_number['main']
            for existing_number in existing_numbers
            if existing_number['tenant_uuid'] == number['tenant_uuid']
        )
    ]
    query = phone_number_table.insert().values(
        number=sa.bindparam('number'),
        tenant_uuid=sa.bindparam('tenant_uuid'),
        caller_id_name=None,
        shared=True,
        main=True
    )
    if actually_new_numbers:
        op.get_bind().execute(query, actually_new_numbers)


def _lastn(number, length):
    return number[len(number) - length:]


def _number_exists(existing_numbers, number_info):
    # Checks if a number is already configured in the phone_number table
    number = number_info['number']
    tenant_uuid = number_info['tenant_uuid']

    tenant_numbers = (
        existing_number
        for existing_number in existing_numbers
        if existing_number['tenant_uuid'] == tenant_uuid
    )
    for existing_number in tenant_numbers:
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
    main_incalls = _get_incall_main_number_by_tenant()

    existing_numbers = _get_existing_phone_numbers()

    main_numbers = [
        {
            'number': incall['exten'],
            'tenant_uuid': tenant_uuid,
        }
        for tenant_uuid, incall in main_incalls.items()
        if incall['exten'] and VALID_PHONE_NUMBER_RE.match(incall['exten'])
    ]
    _insert_main_phone_numbers(existing_numbers, main_numbers)


def downgrade():
    pass
