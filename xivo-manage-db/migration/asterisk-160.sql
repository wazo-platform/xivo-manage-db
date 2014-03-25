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


/* insert destination type only if it doesn't already exist */
INSERT INTO "func_key_destination_type" (id, name)
SELECT
    3, 'queue'
WHERE NOT EXISTS (
    SELECT * FROM "func_key_destination_type"
    WHERE "id" = 3
    AND "name" = 'queue'
);


DROP TABLE IF EXISTS "func_key_dest_queue" CASCADE;
CREATE TABLE "func_key_dest_queue" (
    "func_key_id"               INTEGER         NOT NULL,
    "destination_type_id"       INTEGER         NOT NULL        DEFAULT 3       CHECK ("destination_type_id" = 3),
    "queue_id"                  INTEGER         NOT NULL        REFERENCES "queuefeatures"("id"),

    PRIMARY KEY("func_key_id", "destination_type_id", "queue_id"),
    FOREIGN KEY("func_key_id", "destination_type_id") REFERENCES "func_key"("id", "destination_type_id")
);


GRANT ALL ON "func_key_dest_queue" TO asterisk;

COMMIT;
