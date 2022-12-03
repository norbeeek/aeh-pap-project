-- MySQL Workbench Forward Engineering
CREATE SCHEMA IF NOT EXISTS `library3` DEFAULT CHARACTER SET utf8 ;
USE `library3` ;

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

CREATE TABLE IF NOT EXISTS `library3`.`Books` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `BookName` VARCHAR(150) NOT NULL,
  `AuthorsFirstName` VARCHAR(50) NOT NULL,
  `AuthorsSurname` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `BookID_UNIQUE` (`id` ASC) VISIBLE)
ENGINE = InnoDB;

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


-- DODANIE KONT --
CREATE USER 'user2'@'localhost' IDENTIFIED BY 'user2';
GRANT SELECT ON library3.books TO 'user2'@'localhost';
GRANT SELECT,INSERT,DELETE ON library3.favourites TO 'user2'@'localhost';

CREATE USER 'admin2'@'localhost' IDENTIFIED BY 'adminpass2';
GRANT SELECT,INSERT,DELETE,UPDATE ON library3.books TO 'admin2'@'localhost';
GRANT SELECT,INSERT,DELETE,UPDATE ON library3.favourites TO 'admin2'@'localhost';
GRANT SELECT,INSERT,DELETE,UPDATE ON library3.user TO 'admin2'@'localhost';

CREATE USER 'login2'@'localhost' IDENTIFIED BY 'loginpass2';
GRANT SELECT,INSERT ON library3.user TO 'login3'@'localhost';

-- WYPEŁNIENIE LIB --

INSERT INTO User (email,name,password, isAdmin) VALUES ("admin@admin.pl","admin","sha256$ysqmqXxHAjxs70gr$d085cc7eca7f1b4fb49787685b9644620dabc52b9ceb1326892e51904069563c",TRUE);
INSERT INTO Books (BookName,AuthorsFirstName,AuthorsSurname) VALUES ("Call of Cthulhu","Howard","Lovecraft");
INSERT INTO Books (BookName,AuthorsFirstName,AuthorsSurname) VALUES ("Dune","Frank","Herbert");
INSERT INTO Books (BookName,AuthorsFirstName,AuthorsSurname) VALUES ("Game of thrones","George","Martin");
INSERT INTO Books (BookName,AuthorsFirstName,AuthorsSurname) VALUES ("Harry Potter","J.K.","Rowling");
INSERT INTO Books (BookName,AuthorsFirstName,AuthorsSurname) VALUES ("The Witcher","Andrzej","Sapkowski");
INSERT INTO Favourites(User_id,Books_id) VALUES (1,1);
INSERT INTO Favourites(User_id,Books_id) VALUES (4,1);
INSERT INTO Favourites(User_id,Books_id) VALUES (5,2);
INSERT INTO Favourites(User_id,Books_id) VALUES (5,3);
