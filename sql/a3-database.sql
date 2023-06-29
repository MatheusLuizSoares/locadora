-- Adminer 4.8.1 MySQL 8.0.33 dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP DATABASE IF EXISTS `a3-database-2`;
CREATE DATABASE `a3-database-2`;
USE `a3-database-2`;

DROP TABLE IF EXISTS `movies`;
CREATE TABLE `movies` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) CHARACTER SET utf8mb4 NOT NULL,
  `year` varchar(4) NOT NULL,
  `genre` varchar(255) NOT NULL,
  `rent_price` int NOT NULL,
  `photo` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `movies` (`id`, `title`, `year`, `genre`, `rent_price`, `photo`, `created_at`, `updated_at`) VALUES
(3,	'Blade Runner',	'1982',	'Sci-fi',	8,	'1686861170.1384575.jpg',	'2023-06-15 20:32:50',	'2023-06-15 20:32:50'),
(4,	'Clube da Luta',	'1999',	'Drama',	12,	'1686862110.7634618.jpg',	'2023-06-15 20:48:31',	'2023-06-15 20:48:31'),
(7,	'Harry Potter e a Pedra Filosofal',	'2001',	'Fantasia',	12,	'1686867061.695101.jpg',	'2023-06-15 22:11:02',	'2023-06-15 22:11:02'),
(9,	'O Auto da Compadecida',	'2001',	'Aventura',	12,	'1686867258.7625673.jpeg',	'2023-06-15 22:14:19',	'2023-06-15 22:14:19'),
(10,	'Deadpool',	'2016',	'Comédia',	7,	'1686867388.1376388.png',	'2023-06-15 22:16:28',	'2023-06-15 22:16:28'),
(11,	'Velozes e Furiosos',	'2001',	'Aventura',	14,	'1686867479.2029262.png',	'2023-06-15 22:17:59',	'2023-06-15 22:17:59'),
(12,	'Barbie e o Portal Secreto',	'2014',	'Ação',	8,	'1686867542.9826636.jpg',	'2023-06-15 22:19:20',	'2023-06-15 22:19:20'),
(13,	'Shrek',	'2001',	'Comédia',	21,	'1686867636.2314384.png',	'2023-06-15 22:20:36',	'2023-06-15 22:20:36')
ON DUPLICATE KEY UPDATE `id` = VALUES(`id`), `title` = VALUES(`title`), `year` = VALUES(`year`), `genre` = VALUES(`genre`), `rent_price` = VALUES(`rent_price`), `photo` = VALUES(`photo`), `created_at` = VALUES(`created_at`), `updated_at` = VALUES(`updated_at`);

DROP TABLE IF EXISTS `rents`;
CREATE TABLE `rents` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `movie_id` int NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `rents` (`id`, `user_id`, `movie_id`, `created_at`, `updated_at`) VALUES
(3,	17,	4,	'2023-06-15 21:01:18',	'2023-06-15 18:01:18'),
(4,	17,	7,	'2023-06-15 22:31:36',	'2023-06-15 19:31:36')
ON DUPLICATE KEY UPDATE `id` = VALUES(`id`), `user_id` = VALUES(`user_id`), `movie_id` = VALUES(`movie_id`), `created_at` = VALUES(`created_at`), `updated_at` = VALUES(`updated_at`);

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `cpf` varchar(11) CHARACTER SET utf8mb4 NOT NULL,
  `birth_date` timestamp NOT NULL,
  `photo` varchar(255) CHARACTER SET utf8mb4 DEFAULT NULL,
  `password` varchar(255) NOT NULL,
  `access` varchar(10) CHARACTER SET utf8mb4 NOT NULL DEFAULT 'client',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `users` (`id`, `name`, `email`, `cpf`, `birth_date`, `photo`, `password`, `access`, `created_at`, `updated_at`) VALUES
(17,	'admin',	'admin@flaxflix.com',	'16726336055',	'2023-06-24 03:00:00',	NULL,	'$2b$12$w7UwauV98eM76jEbhghUM.8o1HZbJiRSvEUiHelbQybSJVsDqQNWe',	'admin',	'2023-06-15 11:52:42',	'2023-06-15 11:52:42')
ON DUPLICATE KEY UPDATE `id` = VALUES(`id`), `name` = VALUES(`name`), `email` = VALUES(`email`), `cpf` = VALUES(`cpf`), `birth_date` = VALUES(`birth_date`), `photo` = VALUES(`photo`), `password` = VALUES(`password`), `access` = VALUES(`access`), `created_at` = VALUES(`created_at`), `updated_at` = VALUES(`updated_at`);

-- 2023-06-15 22:34:58
