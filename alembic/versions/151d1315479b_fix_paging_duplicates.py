"""fix paging duplicates

Revision ID: 151d1315479b
Revises: 2acff5c02871

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = '151d1315479b'
down_revision = '2acff5c02871'


def upgrade():
    query = """
    DO $$

    DECLARE
        created_func_key_id INTEGER;

        broken_pagings CURSOR FOR
            SELECT
                paging_id
            FROM
                func_key_dest_paging
            GROUP BY
                paging_id
            HAVING
                COUNT(func_key_id) > 1
            ;

    BEGIN
        FOR broken_row IN broken_pagings LOOP

            INSERT INTO func_key
                (type_id, destination_type_id)
            VALUES
                (1, 9)
            RETURNING id
            INTO created_func_key_id
            ;

            INSERT INTO func_key_dest_paging
                (func_key_id, paging_id)
            VALUES
                (created_func_key_id, broken_row.paging_id)
            ;

            UPDATE func_key_mapping
            SET
                func_key_id = created_func_key_id
            WHERE
                destination_type_id = 9
                AND func_key_id IN (
                    SELECT
                        func_key_id
                    FROM
                        func_key_dest_paging
                    WHERE
                        paging_id = broken_row.paging_id
                )
            ;

            DELETE FROM func_key_dest_paging
            WHERE
                paging_id = broken_row.paging_id
                AND func_key_id != created_func_key_id
            ;

            DELETE FROM func_key
            WHERE
                destination_type_id = 9
                AND id NOT IN (
                    SELECT
                        func_key_id
                    FROM
                        func_key_dest_paging
                )
            ;

        END LOOP;

    END
    $$;
    """

    op.get_bind().execute(query)


def downgrade():
    pass
