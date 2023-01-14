-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema library3
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema library3
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `library3` DEFAULT CHARACTER SET utf8 ;
USE `library3` ;

-- -----------------------------------------------------
-- Table `library3`.`User`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `library3`.`User` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(50) NOT NULL,
  `name` VARCHAR(50) NOT NULL,
  `password` VARCHAR(150) NOT NULL,
  `isAdmin` TINYINT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `UserID_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `library3`.`Books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `library3`.`Books` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `BookName` VARCHAR(150) NOT NULL,
  `AuthorsFirstName` VARCHAR(50) NOT NULL,
  `AuthorsSurname` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `BookID_UNIQUE` (`id` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `library3`.`Favourites`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `library3`.`Favourites` (
  `User_id` INT NOT NULL,
  `Books_id` INT NOT NULL,
  PRIMARY KEY (`User_id`, `Books_id`),
  INDEX `fk_User_has_Books_Books1_idx` (`Books_id` ASC) VISIBLE,
  INDEX `fk_User_has_Books_User_idx` (`User_id` ASC) VISIBLE,
  CONSTRAINT `fk_User_has_Books_User`
    FOREIGN KEY (`User_id`)
    REFERENCES `library3`.`User` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_User_has_Books_Books1`
    FOREIGN KEY (`Books_id`)
    REFERENCES `library3`.`Books` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
