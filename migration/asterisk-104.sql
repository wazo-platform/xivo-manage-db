/*
 * XiVO Base-Config
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

CREATE OR REPLACE FUNCTION "set_agent_on_pauseall" ()
  RETURNS trigger AS
$$
DECLARE
    "number" text;
BEGIN
    SELECT "agent_number" INTO "number" FROM "agent_login_status" WHERE "interface" = NEW."agent";
    IF FOUND THEN
        NEW."agent" := 'Agent/' || "number";
    END IF;

    RETURN NEW;
END;
$$
LANGUAGE plpgsql;

CREATE TRIGGER "change_queue_log_agent"
    BEFORE INSERT ON "queue_log"
    FOR EACH ROW
    WHEN (NEW."event" = 'PAUSEALL' OR NEW."event" = 'UNPAUSEALL')
    EXECUTE PROCEDURE "set_agent_on_pauseall"();

COMMIT;
