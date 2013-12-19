/*
 * Copyright (C) 2012  Avencall
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License AS published by
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

DROP TABLE IF EXISTS "call_log" CASCADE;
CREATE TABLE "call_log" (
 "id" SERIAL PRIMARY KEY,
 "date" TIMESTAMP NOT NULL,
 "source_name" VARCHAR(255),
 "source_exten" VARCHAR(255),
 "destination_name" VARCHAR(255),
 "destination_exten" VARCHAR(255),
 "duration" INTERVAL NOT NULL,
 "user_field" VARCHAR(255),
 "answered" BOOLEAN
);

DROP TABLE IF EXISTS "cel_call_log" CASCADE;
CREATE TABLE "cel_call_log" (
       "cel_id" INTEGER REFERENCES "cel"("id") ON DELETE CASCADE UNIQUE,
       "call_log_id" INTEGER REFERENCES "call_log"("id") ON DELETE CASCADE,
       PRIMARY KEY("cel_id", "call_log_id")
);


GRANT ALL ON "call_log_id_seq" TO asterisk;
GRANT ALL ON "call_log" TO asterisk;
GRANT ALL ON "cel_call_log" TO asterisk;

COMMIT;

