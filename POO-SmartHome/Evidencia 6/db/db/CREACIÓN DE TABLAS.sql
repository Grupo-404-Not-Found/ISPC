-- ============================================================
-- Esquema SmartHome (coherente con UML y buenas prácticas)
-- Español (snake_case), FKs con ON DELETE/UPDATE, índices,
-- ENUM para dominios, UNIQUE en numero_serie, tabla puente N..N
-- ============================================================

-- Usuarios
CREATE TABLE IF NOT EXISTS usuarios (
  id              INT PRIMARY KEY AUTO_INCREMENT,
  username        VARCHAR(50)  NOT NULL UNIQUE,
  email           VARCHAR(100) NOT NULL UNIQUE,
  role            VARCHAR(50),
  password_hash   VARCHAR(255) NOT NULL,
  created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Terminales
CREATE TABLE IF NOT EXISTS terminales (
  terminal_id     INT PRIMARY KEY AUTO_INCREMENT,
  user_id         INT NOT NULL,
  terminal_name   VARCHAR(100) NOT NULL,
  location        VARCHAR(100),
  created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_terminal_usuario
    FOREIGN KEY (user_id) REFERENCES usuarios(id)
    ON DELETE CASCADE ON UPDATE CASCADE
);

-- Dispositivos
CREATE TABLE IF NOT EXISTS dispositivos (
  device_id       INT PRIMARY KEY AUTO_INCREMENT,
  terminal_id     INT NOT NULL,
  user_id         INT NOT NULL,
  nombre          VARCHAR(50) NOT NULL,
  tipo            VARCHAR(30),
  numero_serie    VARCHAR(100) NOT NULL,
  estado          ENUM('activo','inactivo') DEFAULT 'activo',
  metadata        JSON,
  created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT uk_dispositivo_numero_serie UNIQUE (numero_serie),
  INDEX idx_dispositivo_terminal (terminal_id),
  INDEX idx_dispositivo_usuario (user_id),
  CONSTRAINT fk_dispositivo_terminal
    FOREIGN KEY (terminal_id) REFERENCES terminales(terminal_id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_dispositivo_usuario
    FOREIGN KEY (user_id) REFERENCES usuarios(id)
    ON DELETE CASCADE ON UPDATE CASCADE
);

-- Cámaras (extensión de dispositivo)
CREATE TABLE IF NOT EXISTS camaras (
  camera_id       INT PRIMARY KEY AUTO_INCREMENT,
  device_id       INT NOT NULL,
  nombre          VARCHAR(100) NOT NULL,
  estado          ENUM('grabando','apagada','en_espera') DEFAULT 'apagada',
  file_path       VARCHAR(150) NOT NULL,
  timestamp       DATETIME DEFAULT CURRENT_TIMESTAMP,
  INDEX idx_camara_device (device_id),
  CONSTRAINT fk_camara_dispositivo
    FOREIGN KEY (device_id) REFERENCES dispositivos(device_id)
    ON DELETE CASCADE ON UPDATE CASCADE
);

-- Dispositivos móviles por usuario
CREATE TABLE IF NOT EXISTS dispositivos_moviles (
  movil_id        INT PRIMARY KEY AUTO_INCREMENT,
  user_id         INT NOT NULL,
  nombre          VARCHAR(50) NOT NULL,
  sistema_operativo VARCHAR(50),
  permisos        ENUM('admin','lectura','escritura') DEFAULT 'lectura',
  last_used       TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  INDEX idx_movil_usuario (user_id),
  CONSTRAINT fk_movil_usuario
    FOREIGN KEY (user_id) REFERENCES usuarios(id)
    ON DELETE CASCADE ON UPDATE CASCADE
);

-- Automatizaciones
CREATE TABLE IF NOT EXISTS automatizaciones (
  automatizacion_id INT PRIMARY KEY AUTO_INCREMENT,
  nombre            VARCHAR(100) NOT NULL,
  descripcion       VARCHAR(255)
);

-- Relación N..N Automatización ↔ Dispositivo
CREATE TABLE IF NOT EXISTS automatizacion_dispositivo (
  automatizacion_id INT NOT NULL,
  device_id         INT NOT NULL,
  PRIMARY KEY (automatizacion_id, device_id),
  CONSTRAINT fk_ad_automatizacion
    FOREIGN KEY (automatizacion_id) REFERENCES automatizaciones(automatizacion_id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_ad_dispositivo
    FOREIGN KEY (device_id) REFERENCES dispositivos(device_id)
    ON DELETE CASCADE ON UPDATE CASCADE
);
