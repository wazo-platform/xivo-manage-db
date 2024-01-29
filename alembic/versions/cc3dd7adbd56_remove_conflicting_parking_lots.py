"""remove conflicting parking lots

Revision ID: cc3dd7adbd56
Revises: f64ea9c1a1d3

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc3dd7adbd56'
down_revision = 'f64ea9c1a1d3'

parking_lot_table = sa.sql.table(
    'parking_lot',
    sa.sql.column('id'),
    sa.sql.column('slots_start'),
    sa.sql.column('slots_end'),
)

extensions_table = sa.sql.table(
    'extensions',
    sa.sql.column('id'),
    sa.sql.column('context'),
    sa.sql.column('type'),
    sa.sql.column('typeval'),
)


def upgrade():
    query = sa.sql.select(
        [
            parking_lot_table.c.id.label('id'),
            parking_lot_table.c.slots_start.label('slots_start'),
            parking_lot_table.c.slots_end.label('slots_end'),
            extensions_table.c.context.label('context'),
        ],
        from_obj=[
            parking_lot_table.join(
                extensions_table,
                sa.sql.and_(
                    (
                        sa.sql.cast(parking_lot_table.c.id, sa.String)
                        == extensions_table.c.typeval
                    ),
                    extensions_table.c.type == 'parking',
                ),
            )
        ],
    ).order_by(parking_lot_table.c.id)
    parking_lots = list(op.get_bind().execute(query))

    for parking_lot in parking_lots:
        sibling_parking_lots = list(
            sibling_parking_lot
            for sibling_parking_lot in parking_lots
            if (
                # Since IDs are ordered, we can compare them to avoid:
                # 1. conflicting with ourselves (A.id != B.id)
                # 2. checking twice for conflicts (A vs B) and (B vs A)
                parking_lot.id < sibling_parking_lot.id
                and parking_lot.context == sibling_parking_lot.context
            )
        )
        for sibling_parking_lot in sibling_parking_lots:
            if _parking_lot_conflict(parking_lot, sibling_parking_lot):
                # if conflict, no parking can work, let's delete them both
                _delete_parking_lot(parking_lot.id)
                _delete_parking_lot(sibling_parking_lot.id)


def _parking_lot_conflict(parking_lot, sibling_parking_lot):
    if parking_lot.slots_start < sibling_parking_lot.slots_start:
        lower_parking_lot = parking_lot
        upper_parking_lot = sibling_parking_lot
    else:
        lower_parking_lot = sibling_parking_lot
        upper_parking_lot = parking_lot

    expected_order = [
        lower_parking_lot.slots_start,
        lower_parking_lot.slots_end,
        upper_parking_lot.slots_start,
        upper_parking_lot.slots_end,
    ]
    return (
        expected_order != sorted(expected_order)
        or lower_parking_lot.slots_end == upper_parking_lot.slots_start
    )


def _delete_parking_lot(parking_lot_id):
    # delete extension
    query = (
        extensions_table.delete()
        .where(extensions_table.c.type == 'parking')
        .where(extensions_table.c.typeval == str(parking_lot_id))
    )
    op.execute(query)

    # delete parking lot
    query = parking_lot_table.delete().where(parking_lot_table.c.id == parking_lot_id)
    op.execute(query)

    # parking lot funckeys have already been deleted in migration f64ea9c1a1d3


def downgrade():
    pass
