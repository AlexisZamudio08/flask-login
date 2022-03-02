CREATE DATABASE dbo

CREATE TABLE `dbo`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `full_name` VARCHAR(45) NOT NULL,
  `username` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE);

INSERT INTO `dbo`.`user` (`id`, `full_name`, `username`, `password`) VALUES ('1', 'Lorem impsu', 'admin', 'pbkdf2:sha256:260000$vAJQWC0ch9RNfk7c$ca35a8b0f1f0e488fb80d537d379a8be41143a80558049209d2d445b825b6dfc');

COMMIT