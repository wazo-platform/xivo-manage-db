INSERT INTO "tenant" (uuid) VALUES ('eeeeeeee-eeee-eeee-eeee-eeeeeeeeeee1');
INSERT INTO "entity" (name, displayname, description, tenant_uuid) VALUES ('xivotest', 'xivotest', '', 'eeeeeeee-eeee-eeee-eeee-eeeeeeeeeee1');

INSERT INTO "context" (name, displayname, contexttype, description, entity, tenant_uuid)
VALUES
('default', 'Default', 'internal', '', 'xivotest', 'eeeeeeee-eeee-eeee-eeee-eeeeeeeeeee1'),
('from-extern', 'Incalls', 'incall', '', 'xivotest', 'eeeeeeee-eeee-eeee-eeee-eeeeeeeeeee1'),
('to-extern', 'Outcalls', 'outcall', '', 'xivotest', 'eeeeeeee-eeee-eeee-eeee-eeeeeeeeeee1');

INSERT INTO "contextinclude" (context, include) VALUES ('default', 'to-extern');

INSERT INTO "contextnumbers" (context, type, numberbeg, numberend, didlength)
VALUES
('default', 'user', '1000', '1999', 0),
('default', 'group', '2000', '2999', 0),
('default', 'queue', '3000', '3999', 0),
('default', 'meetme', '4000', '4999', 0),
('from-extern', 'incall', '1000', '9999', 0);

INSERT INTO "netiface" (ifname, networktype, type, family, options) VALUES ('eth0', 'voip', 'iface', 'inet', '');

UPDATE provisioning set net4_ip_rest='provd';

ALTER ROLE asterisk WITH SUPERUSER;
