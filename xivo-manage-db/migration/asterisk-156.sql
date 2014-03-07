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
