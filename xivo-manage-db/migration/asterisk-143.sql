/*
 * Copyright (C) 2013  Avencall
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

-- Add the columns allow and disallow to sccpline

DO $$
	BEGIN

		BEGIN
			ALTER TABLE "sccpline" ADD COLUMN "disallow" varchar(100);
		EXCEPTION
			WHEN duplicate_column THEN RAISE NOTICE 'column <disallow> already exists in <sccpline>.';
		END;

		BEGIN
			ALTER TABLE "sccpline" ADD COLUMN "allow" text;
		EXCEPTION
			WHEN duplicate_column THEN RAISE NOTICE 'column <allow> already exists in <sccpline>.';
		END;

	END;
$$;

COMMIT;
