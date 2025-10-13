-- =======================================
-- 1) INSERTS
-- =======================================

-- Usuarios (>=10)
INSERT INTO usuarios (username, email, role, password_hash, created_at) VALUES
('admin', 'admin@example.com', 'administrator', 'hash_admin', NOW()),
('juan', 'juan@example.com', 'user', 'hash1', NOW()),
('maria', 'maria@example.com', 'user', 'hash2', NOW()),
('luis', 'luis@example.com', 'user', 'hash3', NOW()),
('ana', 'ana@example.com', 'user', 'hash4', NOW()),
('rodrigo', 'rodrigo@example.com', 'user', 'hash5', NOW()),
('sofia', 'sofia@example.com', 'user', 'hash6', NOW()),
('carlos', 'carlos@example.com', 'user', 'hash7', NOW()),
('valentina', 'valentina@example.com', 'user', 'hash8', NOW()),
('pedro', 'pedro@example.com', 'user', 'hash9', NOW());

-- Terminales (>=5)
INSERT INTO terminales (user_id, terminal_name, location, created_at) VALUES
(1, 'Terminal Central', 'Comedor', NOW()),
(2, 'Terminal Norte',   'Cocina',  NOW()),
(3, 'Terminal Sur',     'Entrada', NOW()),
(4, 'Terminal Este',    'Oficina', NOW()),
(5, 'Terminal Oeste',   'Garaje',  NOW());

-- Dispositivos (>=10)
INSERT INTO dispositivos (terminal_id, user_id, nombre, tipo, numero_serie, estado, metadata, created_at) VALUES
(1, 1, 'Sensor Puerta',   'Sensor',        'SN-001', 'activo',   JSON_OBJECT('version','1.0','fabricante','ACME'), NOW()),
(2, 2, 'Control Clima',   'Controlador',   'SN-002', 'inactivo', JSON_OBJECT('version','2.0','fabricante','ThermoX'), NOW()),
(1, 3, 'CamBox 1',        'Cámara',        'SN-003', 'activo',   JSON_OBJECT('version','1.5','fabricante','CamTech'), NOW()),
(2, 1, 'Sensor Humo',     'Sensor',        'SN-004', 'activo',   JSON_OBJECT('version','3.0','fabricante','SafeCorp'), NOW()),
(1, 2, 'Control Luces',   'Controlador',   'SN-005', 'inactivo', JSON_OBJECT('version','2.5','fabricante','BrightInc'), NOW()),
(2, 3, 'CamBox 2',        'Cámara',        'SN-006', 'activo',   JSON_OBJECT('version','1.2','fabricante','CamTech'), NOW()),
(1, 4, 'CamBox 3',        'Cámara',        'SN-007', 'activo',   JSON_OBJECT('version','1.3','fabricante','CamTech'), NOW()),
(2, 5, 'Sensor Presencia','Sensor',        'SN-008', 'inactivo', JSON_OBJECT('version','3.1','fabricante','SafeCorp'), NOW()),
(1, 1, 'Control Riego',   'Controlador',   'SN-009', 'activo',   JSON_OBJECT('version','2.1','fabricante','GreenSys'), NOW()),
(2, 2, 'CamBox 4',        'Cámara',        'SN-010', 'inactivo', JSON_OBJECT('version','1.4','fabricante','CamTech'), NOW());

-- Cámaras (>=10) — ver comentario sobre device_id
INSERT INTO camaras (device_id, nombre, estado, file_path, timestamp) VALUES
(3,  'Camara 1',  'grabando', '/videos/cam1.mp4',  NOW()),
(6,  'Camara 2',  'apagada',  '/videos/cam2.mp4',  NOW()),
(7,  'Camara 3',  'grabando', '/videos/cam3.mp4',  NOW()),
(10, 'Camara 4',  'apagada',  '/videos/cam4.mp4',  NOW()),
(3,  'Camara 5',  'grabando', '/videos/cam5.mp4',  NOW()),
(6,  'Camara 6',  'apagada',  '/videos/cam6.mp4',  NOW()),
(7,  'Camara 7',  'grabando', '/videos/cam7.mp4',  NOW()),
(10, 'Camara 8',  'apagada',  '/videos/cam8.mp4',  NOW()),
(3,  'Camara 9',  'grabando', '/videos/cam9.mp4',  NOW()),
(6,  'Camara 10', 'apagada',  '/videos/cam10.mp4', NOW());

-- Dispositivos móviles (>=6)
INSERT INTO dispositivos_moviles (user_id, nombre, sistema_operativo, permisos, last_used) VALUES
(1, 'iPhone 14',    'iOS',     'admin',   NOW()),
(2, 'Galaxy S22',   'Android', 'lectura', NOW()),
(3, 'Pixel 7',      'Android', 'lectura', NOW()),
(4, 'DESKTOP-01',   'Windows', 'admin',   NOW()),
(5, 'iPad Pro',     'iOS',     'lectura', NOW()),
(2, 'ThinkPad X1',  'Linux',   'admin',   NOW());

-- Automatizaciones (>=1) + relación N..N
INSERT INTO automatizaciones (nombre, descripcion) VALUES
('Ahorro de energia', 'Apaga todo salvo camaras');

INSERT INTO automatizacion_dispositivo (automatizacion_id, device_id) VALUES
(1, 1), (1, 2), (1, 4);

-- =======================================
-- 2) CONSULTAS SIMPLES (una por tabla)
-- =======================================

-- Usuarios con rol admin
SELECT id, username, email FROM usuarios WHERE role = 'administrator';

-- Terminales ubicadas en 'Cocina'
SELECT terminal_id, terminal_name FROM terminales WHERE location = 'Cocina';

-- Dispositivos activos
SELECT device_id, nombre, tipo FROM dispositivos WHERE estado = 'activo';

-- Cámaras 'grabando'
SELECT camera_id, nombre, file_path FROM camaras WHERE estado = 'grabando';

-- Móviles Android
SELECT movil_id, nombre, permisos FROM dispositivos_moviles WHERE sistema_operativo = 'Android';

-- =======================================
-- 3) CONSULTAS MULTITABLA (>= 4 JOIN)
-- =======================================

-- JOIN 1: Usuarios y sus dispositivos
SELECT u.username, d.device_id, d.nombre AS dispositivo, d.tipo
FROM usuarios u
JOIN dispositivos d ON d.user_id = u.id
ORDER BY u.username, d.device_id;

-- JOIN 2: Cámaras por usuario (cadena 3 tablas)
SELECT u.username, d.device_id, c.camera_id, c.nombre AS camara, c.estado
FROM usuarios u
JOIN dispositivos d ON d.user_id = u.id
JOIN camaras c      ON c.device_id = d.device_id
ORDER BY u.username, c.camera_id;

-- JOIN 3: Dispositivos por terminal
SELECT t.terminal_name, t.location, d.device_id, d.nombre AS dispositivo, d.tipo
FROM terminales t
JOIN dispositivos d ON d.terminal_id = t.terminal_id
ORDER BY t.terminal_name, d.device_id;

-- JOIN 4: Automatizaciones con dispositivos asociados (N..N)
SELECT a.automatizacion_id, a.nombre AS automatizacion, d.device_id, d.nombre AS dispositivo
FROM automatizaciones a
JOIN automatizacion_dispositivo ad ON ad.automatizacion_id = a.automatizacion_id
JOIN dispositivos d                 ON d.device_id = ad.device_id
ORDER BY a.automatizacion_id, d.device_id;

-- =======================================
-- 4) SUBCONSULTAS (>= 2)
-- =======================================

-- Subconsulta 1: Usuarios sin dispositivos
SELECT u.id, u.username, u.email
FROM usuarios u
WHERE u.id NOT IN (
  SELECT DISTINCT d.user_id FROM dispositivos d
);

-- Subconsulta 2: Dispositivos con al menos una cámara 'grabando'
SELECT d.device_id, d.nombre, d.tipo
FROM dispositivos d
WHERE d.device_id IN (
  SELECT DISTINCT c.device_id FROM camaras c WHERE c.estado = 'grabando'
);
