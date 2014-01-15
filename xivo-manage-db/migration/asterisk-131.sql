/*
 * Copyright (C) 2013-2014  Avencall
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

DROP VIEW IF EXISTS "user_line" CASCADE;
CREATE TABLE "user_line" (
    "id" SERIAL,
    "user_id" INTEGER NOT NULL,
    "line_id" INTEGER NOT NULL,
    "extension_id" INTEGER NOT NULL,
    "main_user" boolean NOT NULL,
    "main_line" boolean NOT NULL,
  CONSTRAINT "user_line__userfeatures_id_fkey" FOREIGN KEY ("user_id")
      REFERENCES "userfeatures" (id) MATCH SIMPLE,
  CONSTRAINT "user_line__linefeatures_id_fkey" FOREIGN KEY ("line_id")
      REFERENCES "linefeatures" (id) MATCH SIMPLE,
  CONSTRAINT "user_line__extensions_id_fkey" FOREIGN KEY ("extension_id")
      REFERENCES "extensions" (id) MATCH SIMPLE,
 PRIMARY KEY("id", "user_id", "line_id")
);


CREATE UNIQUE INDEX "user_line_extension__uidx__user_id_line_id" ON "user_line"("user_id","line_id");

UPDATE linefeatures SET iduserfeatures = 0 WHERE iduserfeatures <> 0 AND iduserfeatures NOT IN (SELECT id FROM userfeatures);

INSERT INTO "user_line" ("user_id", "line_id", "extension_id", "main_user", "main_line")
SELECT
  "iduserfeatures" AS "user_id",
  "id" AS "line_id",
  (SELECT "id" FROM "extensions"
    WHERE "type"='user'
    AND CAST ("typeval" AS INTEGER) = "linefeatures"."iduserfeatures"
    AND "exten" = "linefeatures"."number") AS "extension_id",
  true,
  true
FROM "linefeatures" WHERE "iduserfeatures" <> 0 AND number <> '';

ALTER TABLE "linefeatures" DROP COLUMN "iduserfeatures";

GRANT ALL ON "user_line" TO asterisk;
GRANT ALL ON ALL SEQUENCES IN SCHEMA public to asterisk;

COMMIT;
