-- Cámaras grabando
SELECT nombre AS camara, estado, file_path
FROM camaras
WHERE estado = 'grabando';

-- Usuarios con rol admin
SELECT username, email, role
FROM usuarios
WHERE role = 'admin';

-- Móviles Android
SELECT nombre AS movil, sistema_operativo, permisos
FROM dispositivos_moviles
WHERE sistema_operativo = 'Android';

-- Dispositivos activos
SELECT nombre AS dispositivo, tipo, estado
FROM dispositivos
WHERE estado = 'activo';

-- Terminales en Oficina
SELECT terminal_name, location
FROM terminales
WHERE location = 'Oficina';
