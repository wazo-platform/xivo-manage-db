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

ALTER TABLE "user" ADD COLUMN "entity_id" INTEGER DEFAULT NULL REFERENCES "entity"("id") ON DELETE RESTRICT;

DROP TABLE IF EXISTS "entity_filter";
CREATE TABLE "entity_filter" (
 "id" SERIAL,
 "entity_id" INTEGER NOT NULL REFERENCES "entity"("id") ON DELETE CASCADE,
 "user_id" INTEGER DEFAULT NULL REFERENCES "userfeatures"("id") ON DELETE CASCADE,
 "line_id" INTEGER DEFAULT NULL REFERENCES "linefeatures"("id") ON DELETE CASCADE,
 "queue_id" INTEGER DEFAULT NULL REFERENCES "queuefeatures"("id") ON DELETE CASCADE,
 "group_id" INTEGER DEFAULT NULL REFERENCES "groupfeatures"("id") ON DELETE CASCADE,
 "agent_id" INTEGER DEFAULT NULL REFERENCES "agentfeatures"("id") ON DELETE CASCADE,
 "meetme_id" INTEGER DEFAULT NULL REFERENCES "meetmefeatures"("id") ON DELETE CASCADE,
 "voicemail_id" INTEGER DEFAULT NULL REFERENCES "voicemail"("uniqueid") ON DELETE CASCADE,
 "incall_id" INTEGER DEFAULT NULL REFERENCES "incall"("id") ON DELETE CASCADE,
 "callfilter_id" INTEGER DEFAULT NULL REFERENCES "callfilter"("id") ON DELETE CASCADE,
 "pickup_id" INTEGER DEFAULT NULL REFERENCES "pickup"("id") ON DELETE CASCADE,
 "schedule_id" INTEGER DEFAULT NULL REFERENCES "schedule"("id") ON DELETE CASCADE,
 "device_id" VARCHAR(32) DEFAULT NULL,
 PRIMARY KEY("id")
);

COMMIT;