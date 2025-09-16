-- Usuarios
INSERT INTO usuarios (username, email, role, password_hash, created_at) VALUES
('admin', 'admin@example.com', 'administrator', 'hash123', NOW()),
('juanperez', 'juan@example.com', 'user', 'hash456', NOW()),
('maria', 'maria@example.com', 'user', 'hash789', NOW()),
('ana', 'ana@example.com', 'user', 'hash910', NOW()),
('luis', 'luis@example.com', 'user', 'hash101', NOW());

-- Terminales
INSERT INTO terminales (user_id, terminal_name, location, created_at) VALUES
(1, 'Terminal Central', 'Comedor', NOW()),
(2, 'Terminal Norte',   'Cocina',  NOW()),
(3, 'Terminal Sur',     'Entrada', NOW());

-- Dispositivos (IDs explícitos compatibles con AUTO_INCREMENT)
INSERT INTO dispositivos (device_id, terminal_id, user_id, nombre, tipo, numero_serie, estado, metadata, created_at) VALUES
(100, 1, 1, 'Dispositivo A', 'Sensor',      'SN-001', 'activo',   JSON_OBJECT('version','1.0','fabricante','ACME'), NOW()),
(101, 2, 2, 'Dispositivo B', 'Controlador', 'SN-002', 'inactivo', JSON_OBJECT('version','2.0','fabricante','XYZ'),  NOW()),
(102, 1, 3, 'Dispositivo C', 'Cámara',      'SN-003', 'activo',   JSON_OBJECT('version','1.5','fabricante','CamTech'), NOW()),
(103, 2, 1, 'Dispositivo D', 'Sensor',      'SN-004', 'activo',   JSON_OBJECT('version','3.0','fabricante','SensorCorp'), NOW()),
(104, 1, 2, 'Dispositivo E', 'Controlador', 'SN-005', 'inactivo', JSON_OBJECT('version','2.5','fabricante','ControlInc'), NOW()),
(105, 2, 3, 'Dispositivo F', 'Cámara',      'SN-006', 'activo',   JSON_OBJECT('version','1.2','fabricante','CamTech'), NOW()),
(106, 1, 4, 'Dispositivo G', 'Cámara',      'SN-007', 'activo',   JSON_OBJECT('version','1.3','fabricante','CamTech'), NOW()),
(107, 2, 5, 'Dispositivo H', 'Sensor',      'SN-008', 'inactivo', JSON_OBJECT('version','3.1','fabricante','SensorCorp'), NOW()),
(108, 1, 1, 'Dispositivo I', 'Controlador', 'SN-009', 'activo',   JSON_OBJECT('version','2.1','fabricante','ControlInc'), NOW()),
(109, 2, 2, 'Dispositivo J', 'Cámara',      'SN-010', 'inactivo', JSON_OBJECT('version','1.4','fabricante','CamTech'), NOW());

-- Cámaras
INSERT INTO camaras (device_id, nombre, estado, file_path, timestamp) VALUES
(100, 'Camara 1',  'grabando', '/videos/cam1.mp4',  NOW()),
(101, 'Camara 2',  'apagada',  '/videos/cam2.mp4',  NOW()),
(102, 'Camara 3',  'grabando', '/videos/cam3.mp4',  NOW()),
(103, 'Camara 4',  'apagada',  '/videos/cam4.mp4',  NOW()),
(104, 'Camara 5',  'grabando', '/videos/cam5.mp4',  NOW()),
(105, 'Camara 6',  'apagada',  '/videos/cam6.mp4',  NOW()),
(106, 'Camara 7',  'grabando', '/videos/cam7.mp4',  NOW()),
(107, 'Camara 8',  'apagada',  '/videos/cam8.mp4',  NOW()),
(108, 'Camara 9',  'grabando', '/videos/cam9.mp4',  NOW()),
(109, 'Camara 10', 'apagada',  '/videos/cam10.mp4', NOW());

-- Dispositivos móviles
INSERT INTO dispositivos_moviles (user_id, nombre, sistema_operativo, permisos, last_used) VALUES
(1, 'iPhone 14',      'iOS',     'admin',   NOW()),
(2, 'Samsung Galaxy', 'Android', 'lectura', NOW()),
(3, 'Google Pixel',   'Android', 'lectura', NOW()),
(4, 'DESKTOP-1234',   'Windows', 'admin',   NOW());

-- Usuarios adicionales
INSERT INTO usuarios (username, email, role, password_hash, created_at) VALUES
('sofia', 'sofia@example.com', 'user', 'hash111', NOW()),
('carlos', 'carlos@example.com', 'user', 'hash112', NOW()),
('valentina', 'valentina@example.com', 'user', 'hash113', NOW()),
('pedro', 'pedro@example.com', 'user', 'hash114', NOW());

-- Terminales adicionales
INSERT INTO terminales (user_id, terminal_name, location, created_at) VALUES
(3, 'Terminal Este',  'Oficina', NOW()),
(4, 'Terminal Oeste', 'Garaje',  NOW());

-- Dispositivos adicionales
INSERT INTO dispositivos (device_id, terminal_id, user_id, nombre, tipo, numero_serie, estado, metadata, created_at) VALUES
(110, 1, 1, 'Dispositivo K', 'Sensor',      'SN-011', 'activo',   JSON_OBJECT('version','4.0','fabricante','ACME'),      NOW()),
(111, 2, 2, 'Dispositivo L', 'Cámara',      'SN-012', 'inactivo', JSON_OBJECT('version','1.6','fabricante','CamTech'),  NOW()),
(112, 1, 3, 'Dispositivo M', 'Controlador', 'SN-013', 'activo',   JSON_OBJECT('version','2.6','fabricante','ControlInc'),NOW());

-- Cámaras adicionales
INSERT INTO camaras (device_id, nombre, estado, file_path, timestamp) VALUES
(110, 'Camara 11', 'grabando', '/videos/cam11.mp4', NOW()),
(111, 'Camara 12', 'apagada',  '/videos/cam12.mp4', NOW()),
(112, 'Camara 13', 'grabando', '/videos/cam13.mp4', NOW());

-- Dispositivos móviles adicionales
INSERT INTO dispositivos_moviles (user_id, nombre, sistema_operativo, permisos, last_used) VALUES
(5, 'iPad Pro',      'iOS',     'lectura', NOW()),
(2, 'Huawei P50',    'Android', 'admin',   NOW()),
(3, 'MacBook Air',   'macOS',   'lectura', NOW()),
(4, 'ThinkPad X1',   'Linux',   'admin',   NOW()),
(6, 'alienware',     'Windows', 'lectura', NOW());

-- Automatizaciones + relación con dispositivos (coherente con UML)
INSERT INTO automatizaciones (nombre, descripcion) VALUES
('Ahorro de energia', 'Apaga todo salvo camaras');

INSERT INTO automatizacion_dispositivo (automatizacion_id, device_id) VALUES
(1, 100), (1, 101), (1, 102);