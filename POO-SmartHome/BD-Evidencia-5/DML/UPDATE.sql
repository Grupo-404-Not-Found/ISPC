UPDATE dispositivos_moviles
SET permisos = 'admin'
WHERE nombre = 'Samsung Galaxy';

UPDATE usuarios
SET role = 'admin', email = 'sofia@example.com'
WHERE username = 'sofia';

UPDATE terminales
SET location = 'Recepción'
WHERE terminal_name = 'Terminal Oeste';

UPDATE dispositivos
SET estado = 'inactivo'
WHERE nombre = 'Dispositivo K';

UPDATE camaras
SET estado = 'apagada'
WHERE nombre = 'Camara 11';

UPDATE dispositivos_moviles
SET last_used = NOW()
WHERE nombre = 'iPad Pro';