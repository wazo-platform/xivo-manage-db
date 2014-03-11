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
    2, 'group'
WHERE NOT EXISTS (
    SELECT * FROM "func_key_destination_type"
    WHERE "id" = 2
    AND "name" = 'group'
);


DROP TABLE IF EXISTS "func_key_dest_group" CASCADE;
CREATE TABLE "func_key_dest_group" (
    "func_key_id"               INTEGER         NOT NULL,
    "destination_type_id"       INTEGER         NOT NULL        DEFAULT 2       CHECK ("destination_type_id" = 2),
    "group_id"                  INTEGER         NOT NULL        REFERENCES "groupfeatures"("id"),

    PRIMARY KEY("func_key_id", "destination_type_id", "group_id"),
    FOREIGN KEY("func_key_id", "destination_type_id") REFERENCES "func_key"("id", "destination_type_id")
);


GRANT ALL ON "func_key_dest_group" TO asterisk;

COMMIT;
