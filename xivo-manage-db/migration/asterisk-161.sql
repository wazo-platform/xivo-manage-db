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
    queue_destination_type_id INTEGER;

    queues_cursor CURSOR FOR
        SELECT
            queuefeatures.name  AS name,
            queuefeatures.id    AS id
        FROM
            queuefeatures;

    func_keys_cursor CURSOR FOR
        SELECT
            phonefunckey.iduserfeatures                      AS user_id,
            phonefunckey.typevalextenumbersright::INT        AS destination_id,
            phonefunckey.label                               AS label,
            phonefunckey.supervision::BOOLEAN                AS blf,
            phonefunckey.fknum                               AS position,
            userfeatures.func_key_private_template_id        AS private_template_id,
            func_key_dest_queue.func_key_id                  AS func_key_id
        FROM
            phonefunckey
            INNER JOIN userfeatures
                ON phonefunckey.iduserfeatures = userfeatures.id
            INNER JOIN func_key_dest_queue
                ON func_key_dest_queue.queue_id = phonefunckey.typevalextenumbersright::INT
        WHERE
            phonefunckey.typeextenumbersright = 'queue';

BEGIN
    SELECT id FROM func_key_type WHERE name = 'speeddial' INTO STRICT speeddial_type_id;
    SELECT id FROM func_key_destination_type WHERE name = 'queue' INTO STRICT queue_destination_type_id;

    /* delete old func keys that point towards queues that no longer exist */
    DELETE FROM phonefunckey
    WHERE typeextenumbersright = 'queue'
        AND typevalextenumbersright::int NOT IN (SELECT id FROM queuefeatures);

    /* create queue destinations for all queues */
    FOR queue_row IN queues_cursor LOOP

        RAISE NOTICE 'Creating func key for queue "%" (id %)', queue_row.name, queue_row.id;

        /* create func key */
        INSERT INTO func_key
            (type_id, destination_type_id)
        VALUES
            (speeddial_type_id, queue_destination_type_id)
        RETURNING id INTO STRICT created_func_key_id;

        /* associate func key with its destination */
        INSERT INTO func_key_dest_queue
            (func_key_id, queue_id)
        VALUES
            (created_func_key_id, queue_row.id);

    END LOOP;

    /* migrate existing queue func keys into user's private templates */
    FOR func_key_row IN func_keys_cursor LOOP

        RAISE NOTICE 'Migrating func key for user % with destination queue %', func_key_row.user_id, func_key_row.destination_id;

        /* associate queue destinations with user's private template */
        INSERT INTO func_key_mapping
            (template_id, func_key_id, destination_type_id, label, position, blf)
        VALUES
            (
                func_key_row.private_template_id,
                func_key_row.func_key_id,
                queue_destination_type_id,
                func_key_row.label,
                func_key_row.position,
                func_key_row.blf
            );

    END LOOP;

    /* remove old func keys */
    DELETE FROM phonefunckey WHERE typeextenumbersright = 'queue';

END
$$;

COMMIT;
