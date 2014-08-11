/*
 * Copyright (C) 2014  Avencall
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */


BEGIN;

DO $$
DECLARE

    duplicate_cursor CURSOR FOR
        SELECT fk.* FROM
            phonefunckey fk
        INNER JOIN (
            SELECT
        typevalextenumbersright,
                min(fknum) as first_position
            FROM
                phonefunckey
            WHERE
                typeextenumbersright = 'user'
            GROUP BY
                typevalextenumbersright
            having ( count(typevalextenumbersright) > 1 )
        ) AS valid_func_keys
        ON
        fk.typevalextenumbersright = valid_func_keys.typevalextenumbersright
        AND fknum > valid_func_keys.first_position
        AND typeextenumbersright = 'user';

BEGIN


    FOR duplicate_row IN duplicate_cursor LOOP

        RAISE NOTICE '[MIGRATE_FK] : Deleting func key for user "%" (pointing on user id %)', duplicate_row.iduserfeatures, duplicate_row.typevalextenumbersright;

        DELETE FROM
            phonefunckey
        WHERE
            iduserfeatures = duplicate_row.iduserfeatures
        AND
            typeextenumbersright = 'user'
        AND
            typevalextenumbersright = duplicate_row.typevalextenumbersright
        AND
            fknum = duplicate_row.fknum;

    END LOOP;

END
$$;

COMMIT;

BEGIN;

DO $$
DECLARE
    created_func_key_id INTEGER;
    speeddial_type_id INTEGER;
    user_destination_type_id INTEGER;

    user_cursor CURSOR FOR
        SELECT
            userfeatures.id         AS id
        FROM
            userfeatures
        WHERE
            userfeatures.id NOT IN (
                SELECT user_id
                FROM func_key_dest_user
            );

BEGIN
    SELECT id FROM func_key_type WHERE name = 'speeddial' INTO STRICT speeddial_type_id;
    SELECT id FROM func_key_destination_type WHERE name = 'user' INTO STRICT user_destination_type_id;

    FOR user_row IN user_cursor LOOP

        INSERT INTO func_key
            (type_id, destination_type_id)
        VALUES
            (speeddial_type_id, user_destination_type_id)
        RETURNING id INTO STRICT created_func_key_id;

        INSERT INTO func_key_dest_user
            (func_key_id, user_id)
        VALUES
            (created_func_key_id, user_row.id);

    END LOOP;

END
$$;

COMMIT;
