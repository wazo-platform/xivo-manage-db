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

    users_cursor CURSOR FOR
        SELECT DISTINCT
            userfeatures.id                                         AS id,
            userfeatures.firstname || ' ' || userfeatures.lastname  AS name,
            userfeatures.func_key_private_template_id               AS private_template_id
        FROM
            userfeatures
            INNER JOIN phonefunckey
                ON phonefunckey.typeextenumbersright = 'user'
                AND phonefunckey.typeextenumbers IS NULL
                AND phonefunckey.typevalextenumbers IS NULL
                AND userfeatures.id = phonefunckey.iduserfeatures;

    func_keys_cursor CURSOR (selected_user_id INTEGER) FOR
        SELECT
            iduserfeatures                      AS user_id,
            typevalextenumbersright::INT        AS destination_id,
            label                               AS label,
            supervision::BOOLEAN                AS blf,
            fknum                               AS position
        FROM
            phonefunckey
        WHERE
            typeextenumbersright = 'user'
            AND phonefunckey.typeextenumbers IS NULL
            AND phonefunckey.typevalextenumbers IS NULL
            AND iduserfeatures = selected_user_id;

BEGIN
    SELECT id FROM func_key_type WHERE name = 'speeddial' INTO STRICT speeddial_type_id;
    SELECT id FROM func_key_destination_type WHERE name = 'user' INTO STRICT user_destination_type_id;

    /* delete old func keys that point towards users that no longer exist */
    DELETE FROM phonefunckey
    WHERE typeextenumbersright = 'user'
        AND typeextenumbers IS NULL
        AND typevalextenumbers IS NULL
        AND typevalextenumbersright::int NOT IN (SELECT id FROM userfeatures);

    FOR user_row IN users_cursor LOOP

        RAISE NOTICE 'Migrating user func keys for "%" (id %)', user_row.name, user_row.id;

        /* create func keys for user's template */
        FOR func_key_row IN func_keys_cursor(user_row.id) LOOP

            RAISE NOTICE 'func key with destination: user %', func_key_row.destination_id;

            /* start by creating the func key */
            INSERT INTO func_key
                (type_id, destination_type_id)
            VALUES
                (speeddial_type_id, user_destination_type_id)
            RETURNING id INTO STRICT created_func_key_id;

            /* associate func key with user's private template */
            INSERT INTO func_key_mapping
                (template_id, func_key_id, destination_type_id, label, position, blf)
            VALUES
                (user_row.private_template_id,
                 created_func_key_id,
                 user_destination_type_id,
                 func_key_row.label,
                 func_key_row.position,
                 func_key_row.blf);

            /* associate func key with its destination */
            INSERT INTO func_key_dest_user
                (func_key_id, user_id)
            VALUES
                (created_func_key_id, func_key_row.destination_id);

            /* remove old func key */
            DELETE FROM phonefunckey WHERE CURRENT OF func_keys_cursor;

        END LOOP;
    END LOOP;

    /* sanity check: make sure there are no longer any user func keys left */
    PERFORM * FROM phonefunckey WHERE typeextenumbersright = 'user'
                                AND phonefunckey.typeextenumbers IS NULL
                                AND phonefunckey.typevalextenumbers IS NULL;
    IF FOUND THEN
        RAISE EXCEPTION 'Could not convert all user func keys. (check table phonefunckey)';
    END IF;

END
$$;

COMMIT;
