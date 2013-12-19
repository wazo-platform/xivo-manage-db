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

DO $$
  BEGIN

    BEGIN
      ALTER TABLE call_log ADD "source_line_identity" VARCHAR(255);
    EXCEPTION
      WHEN duplicate_column THEN RAISE NOTICE 'column <source_line_identity> already exists in <call_log>.';
    END;

    BEGIN
      ALTER TABLE call_log ADD "destination_line_identity" VARCHAR(255);
    EXCEPTION
      WHEN duplicate_column THEN RAISE NOTICE 'column <destination_line_identity> already exists in <call_log>.';
    END;

  END;
$$;

COMMIT;
