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

/* create tables */

DROP TABLE IF EXISTS "func_key_template" CASCADE;
CREATE TABLE "func_key_template" (
    "id"        SERIAL          PRIMARY KEY,
    "name"      VARCHAR(128)    NOT NULL,
    "private"   BOOLEAN         NOT NULL    DEFAULT FALSE
);

DROP TABLE IF EXISTS "func_key_type" CASCADE;
CREATE TABLE "func_key_type" (
    "id"        SERIAL          PRIMARY KEY,
    "name"      VARCHAR(128)    NOT NULL
);

INSERT INTO "func_key_type" ("name") VALUES ('speeddial');

DROP TABLE IF EXISTS "func_key_destination_type" CASCADE;
CREATE TABLE "func_key_destination_type" (
    "id"        SERIAL          PRIMARY KEY,
    "name"      VARCHAR(128)    NOT NULL
);

INSERT INTO "func_key_destination_type" (id, name) VALUES (1, 'user');

DROP TABLE IF EXISTS "func_key" CASCADE;
CREATE TABLE "func_key" (
    "id"                    SERIAL          NOT NULL,
    "type_id"               INTEGER         NOT NULL    REFERENCES "func_key_type"("id"),
    "destination_type_id"   INTEGER         NOT NULL    REFERENCES "func_key_destination_type"("id"),

    PRIMARY KEY ("id", "destination_type_id")
);

DROP TABLE IF EXISTS "func_key_mapping" CASCADE;
CREATE TABLE "func_key_mapping" (
    "template_id"               INTEGER         REFERENCES "func_key_template"("id"),
    "func_key_id"               INTEGER         NOT NULL,
    "destination_type_id"       INTEGER         NOT NULL,
    "label"                     VARCHAR(128)    NULL,
    "position"                  INTEGER         NOT NULL,
    "blf"                       BOOLEAN         NOT NULL    DEFAULT FALSE,

    PRIMARY KEY("template_id", "func_key_id"),
    FOREIGN KEY("func_key_id", "destination_type_id") REFERENCES "func_key"("id", "destination_type_id"),
    UNIQUE("template_id", "position"),
    CHECK("position" > 0)
);

DROP TABLE IF EXISTS "func_key_dest_user" CASCADE;
CREATE TABLE "func_key_dest_user" (
    "func_key_id"               INTEGER         NOT NULL,
    "user_id"                   INTEGER         NOT NULL        REFERENCES "userfeatures"("id"),
    /* destination_type_id 1 = user (see table func_key_destination_type) */
    "destination_type_id"       INTEGER         NOT NULL        DEFAULT 1       CHECK ("destination_type_id" = 1),

    PRIMARY KEY("func_key_id", "user_id", "destination_type_id"),
    FOREIGN KEY("func_key_id", "destination_type_id") REFERENCES "func_key"("id", "destination_type_id")
);

ALTER TABLE "userfeatures"
    ADD "func_key_template_id"              INTEGER     NULL    REFERENCES "func_key_template"("id"),
    ADD "func_key_private_template_id"      INTEGER     NULL    REFERENCES "func_key_template"("id");

GRANT ALL ON "func_key" TO asterisk;
GRANT ALL ON "func_key_id_seq" TO asterisk;
GRANT ALL ON "func_key_template" TO asterisk;
GRANT ALL ON "func_key_template_id_seq" TO asterisk;
GRANT ALL ON "func_key_type" TO asterisk;
GRANT ALL ON "func_key_type_id_seq" TO asterisk;
GRANT ALL ON "func_key_mapping" TO asterisk;
GRANT ALL ON "func_key_destination_type" TO asterisk;
GRANT ALL ON "func_key_destination_type_id_seq" TO asterisk;
GRANT ALL ON "func_key_dest_user" TO asterisk;

COMMIT;
