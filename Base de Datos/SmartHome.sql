CREATE TABLE `users` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `username` varchar(50) UNIQUE NOT NULL,
  `email` varchar(100) UNIQUE NOT NULL,
  `role` varchar(255),
  `password_hash` varchar(255) NOT NULL,
  `created_at` timestamp
);

CREATE TABLE `devices` (
  `device_id` integer PRIMARY KEY,
  `terminal_id` integer NOT NULL,
  `device_name` varchar(50) NOT NULL,
  `device_type` varchar(30),
  `device_serial_number` varchar(100) NOT NULL,
  `status` varchar(20),
  `user_id` integer NOT NULL,
  `metadata` JSON
);

CREATE TABLE `Cameras` (
  `camera_id` integer PRIMARY KEY AUTO_INCREMENT,
  `device_id` integer NOT NULL,
  `camera_name` varchar(50) NOT NULL,
  `timestamp` datetime,
  `status` varchar(255),
  `file_path` varchar(150) NOT NULL
);

CREATE TABLE `terminal` (
  `terminal_id` integer PRIMARY KEY AUTO_INCREMENT,
  `user_id` integer NOT NULL,
  `terminal_name` varchar(100) NOT NULL,
  `location` varchar(100),
  `created_at` timestamp
);

CREATE TABLE `movil_devices` (
  `movil_device_id` integer PRIMARY KEY AUTO_INCREMENT,
  `user_id` integer NOT NULL,
  `movil_device_name` varchar(50) NOT NULL,
  `os` varchar(50),
  `permissions` varchar(20),
  `last_used` timestamp
);

ALTER TABLE `devices` ADD FOREIGN KEY (`terminal_id`) REFERENCES `terminal` (`terminal_id`);

ALTER TABLE `devices` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `Cameras` ADD FOREIGN KEY (`device_id`) REFERENCES `devices` (`device_id`);

ALTER TABLE `terminal` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `movil_devices` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
