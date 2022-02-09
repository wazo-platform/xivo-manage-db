/* Main tenant */
INSERT INTO "tenant" (uuid) VALUES ('eeeeeeee-eeee-eeee-eeee-eeeeeeeeeee1');

INSERT INTO "endpoint_sip" (label, name, tenant_uuid, template) VALUES ('global', 'ewkxmwye', 'eeeeeeee-eeee-eeee-eeee-eeeeeeeeeee1', true);
INSERT INTO "endpoint_sip" (label, name, tenant_uuid, template) VALUES ('webrtc', 'foobar', 'eeeeeeee-eeee-eeee-eeee-eeeeeeeeeee1', true);
INSERT INTO "endpoint_sip" (label, name, tenant_uuid, template) VALUES ('meeting_guest', 'meeting_guest', 'eeeeeeee-eeee-eeee-eeee-eeeeeeeeeee1', true);
UPDATE "tenant" SET sip_templates_generated = true WHERE "uuid" = 'eeeeeeee-eeee-eeee-eeee-eeeeeeeeeee1';
UPDATE "tenant" SET global_sip_template_uuid = (SELECT "uuid" FROM "endpoint_sip" WHERE "tenant_uuid" = 'eeeeeeee-eeee-eeee-eeee-eeeeeeeeeee1' AND "label" = 'global') WHERE "uuid" = 'eeeeeeee-eeee-eeee-eeee-eeeeeeeeeee1';
UPDATE "tenant" SET webrtc_sip_template_uuid = (SELECT "uuid" FROM "endpoint_sip" WHERE "tenant_uuid" = 'eeeeeeee-eeee-eeee-eeee-eeeeeeeeeee1' AND "label" = 'webrtc') WHERE "uuid" = 'eeeeeeee-eeee-eeee-eeee-eeeeeeeeeee1';
UPDATE "tenant" SET meeting_guest_sip_template_uuid = (SELECT "uuid" FROM "endpoint_sip" WHERE "tenant_uuid" = 'eeeeeeee-eeee-eeee-eeee-eeeeeeeeeee1' AND "label" = 'meeting_guest') WHERE "uuid" = 'eeeeeeee-eeee-eeee-eeee-eeeeeeeeeee1';

INSERT INTO "context" (name, displayname, contexttype, description, tenant_uuid)
VALUES
('default', 'Default', 'internal', '', 'eeeeeeee-eeee-eeee-eeee-eeeeeeeeeee1'),
('from-extern', 'Incalls', 'incall', '', 'eeeeeeee-eeee-eeee-eeee-eeeeeeeeeee1'),
('to-extern', 'Outcalls', 'outcall', '', 'eeeeeeee-eeee-eeee-eeee-eeeeeeeeeee1');

INSERT INTO "contextinclude" (context, include) VALUES ('default', 'to-extern');

INSERT INTO "contextnumbers" (context, type, numberbeg, numberend, didlength)
VALUES
('default', 'user', '1000', '1999', 0),
('default', 'group', '2000', '2999', 0),
('default', 'queue', '3000', '3999', 0),
('default', 'meetme', '4000', '4999', 0),
('from-extern', 'incall', '1000', '9999', 0);

/* Sub tenant */
INSERT INTO "tenant" (uuid) VALUES ('eeeeeeee-eeee-eeee-eeee-eeeeeeeeeee2');

INSERT INTO "endpoint_sip" (label, name, tenant_uuid, template) VALUES ('global', 'sdfgalwe', 'eeeeeeee-eeee-eeee-eeee-eeeeeeeeeee2', true);
INSERT INTO "endpoint_sip" (label, name, tenant_uuid, template) VALUES ('webrtc', 'qpalvkmz', 'eeeeeeee-eeee-eeee-eeee-eeeeeeeeeee2', true);
INSERT INTO "endpoint_sip" (label, name, tenant_uuid, template) VALUES ('meeting_guest', 'woavaldf', 'eeeeeeee-eeee-eeee-eeee-eeeeeeeeeee2', true);
UPDATE "tenant" SET sip_templates_generated = true WHERE "uuid" = 'eeeeeeee-eeee-eeee-eeee-eeeeeeeeeee2';
UPDATE "tenant" SET global_sip_template_uuid = (SELECT "uuid" FROM "endpoint_sip" WHERE "tenant_uuid" = 'eeeeeeee-eeee-eeee-eeee-eeeeeeeeeee2' AND "label" = 'global') WHERE "uuid" = 'eeeeeeee-eeee-eeee-eeee-eeeeeeeeeee2';
UPDATE "tenant" SET webrtc_sip_template_uuid = (SELECT "uuid" FROM "endpoint_sip" WHERE "tenant_uuid" = 'eeeeeeee-eeee-eeee-eeee-eeeeeeeeeee2' AND "label" = 'webrtc') WHERE "uuid" = 'eeeeeeee-eeee-eeee-eeee-eeeeeeeeeee2';
UPDATE "tenant" SET meeting_guest_sip_template_uuid = (SELECT "uuid" FROM "endpoint_sip" WHERE "tenant_uuid" = 'eeeeeeee-eeee-eeee-eeee-eeeeeeeeeee2' AND "label" = 'meeting_guest') WHERE "uuid" = 'eeeeeeee-eeee-eeee-eeee-eeeeeeeeeee2';

INSERT INTO "context" (name, displayname, contexttype, description, tenant_uuid)
VALUES
('default-subtenant', 'Default', 'internal', '', 'eeeeeeee-eeee-eeee-eeee-eeeeeeeeeee2'),
('from-extern-subtenant', 'Incalls', 'incall', '', 'eeeeeeee-eeee-eeee-eeee-eeeeeeeeeee2'),
('to-extern-subtenant', 'Outcalls', 'outcall', '', 'eeeeeeee-eeee-eeee-eeee-eeeeeeeeeee2');

INSERT INTO "contextinclude" (context, include) VALUES ('default-subtenant', 'to-extern-subtenant');

INSERT INTO "contextnumbers" (context, type, numberbeg, numberend, didlength)
VALUES
('default-subtenant', 'user', '1000', '1999', 0),
('default-subtenant', 'group', '2000', '2999', 0),
('default-subtenant', 'queue', '3000', '3999', 0),
('default-subtenant', 'meetme', '4000', '4999', 0),
('from-extern-subtenant', 'incall', '1000', '9999', 0);

INSERT INTO "netiface" (ifname, networktype, type, family, options) VALUES ('eth0', 'voip', 'iface', 'inet', '');

ALTER ROLE asterisk WITH SUPERUSER;
