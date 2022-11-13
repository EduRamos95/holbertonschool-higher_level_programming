-- Creates the table hbtn_0d_usa with table states.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states` (
    PRIMARY KEY(`id`),
    `id`   INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` VARCHAR(256) NOT NULL
);
