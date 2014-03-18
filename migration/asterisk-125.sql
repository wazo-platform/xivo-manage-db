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

ALTER TABLE "extensions" ADD COLUMN "extenhash" VARCHAR(40) NOT NULL DEFAULT '';
ALTER TABLE "extensions" ADD COLUMN "type" extenumbers_type;
ALTER TABLE "extensions" ADD COLUMN "typeval" VARCHAR(255) NOT NULL DEFAULT '';

UPDATE "extensions" 
    SET "extenhash" = "extenumbers"."extenhash",
        "type" = "extenumbers"."type",
        "typeval" = "extenumbers"."typeval"
    FROM "extenumbers" 
    WHERE "extenumbers"."exten" = "extensions"."exten"
    AND "extenumbers"."context" = "extensions"."context"
    AND "extenumbers"."type" <> 'extenfeatures';

UPDATE "extensions" 
    SET "extenhash" = "extenumbers"."extenhash",
        "type" = "extenumbers"."type",
        "typeval" = "extenumbers"."typeval"
    FROM "extenumbers" 
    WHERE "extenumbers"."exten" = "extensions"."exten"
    AND "extenumbers"."type" = 'extenfeatures'
    AND "extenumbers"."typeval" = "extensions"."name";

DROP TABLE IF EXISTS "extenumbers" CASCADE;

DELETE FROM "extensions" WHERE "type" IS NULL;
ALTER TABLE "extensions" ALTER COLUMN "type" SET NOT NULL;
ALTER TABLE "extensions" DROP COLUMN "name";

CREATE INDEX "extensions__idx__exten" ON "extensions"("exten");
CREATE INDEX "extensions__idx__extenhash" ON "extensions"("extenhash");
CREATE INDEX "extensions__idx__context" ON "extensions"("context");
CREATE INDEX "extensions__idx__type" ON "extensions"("type");
CREATE INDEX "extensions__idx__typeval" ON "extensions"("typeval");


UPDATE "ctidirectoryfields" SET "value" = replace("value", 'extenumbers', 'extensions') WHERE "value" LIKE 'extenumbers.%';

UPDATE "extensions" SET "typeval" = (
    SELECT "iduserfeatures" FROM "linefeatures" 
    WHERE CAST("extensions"."typeval"AS INTEGER) = "linefeatures"."id"
    ) 
WHERE "extensions"."type" = 'user';

CREATE UNIQUE INDEX "extensions__uidx__exten_context" ON "extensions"("exten","context");

COMMIT;
