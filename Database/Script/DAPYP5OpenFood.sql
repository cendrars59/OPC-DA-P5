-- MySQL Script generated by MySQL Workbench
-- Mon Dec 30 13:42:15 2019
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema opc_p5_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema opc_p5_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `opc_p5_db` DEFAULT CHARACTER SET utf8mb4 ;
USE `opc_p5_db` ;

-- -----------------------------------------------------
-- Table `opc_p5_db`.`Category`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `opc_p5_db`.`Category` ;

CREATE TABLE IF NOT EXISTS `opc_p5_db`.`Category` (
  `idCategory` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `code` VARCHAR(254) NULL,
  `name` VARCHAR(1024) NULL,
  `url` VARCHAR(1024) NULL,
  `is_active` TINYINT NULL DEFAULT 0,
  PRIMARY KEY (`idCategory`),
  UNIQUE INDEX `idCategorie_UNIQUE` (`idCategory` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `opc_p5_db`.`Store`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `opc_p5_db`.`Store` ;

CREATE TABLE IF NOT EXISTS `opc_p5_db`.`Store` (
  `idStore` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `code` VARCHAR(254) NOT NULL,
  `name` VARCHAR(1024) NULL,
  `url` VARCHAR(1024) NULL,
  `is_active` TINYINT NULL DEFAULT 1,
  PRIMARY KEY (`idStore`),
  UNIQUE INDEX `idStore_UNIQUE` (`idStore` ASC) VISIBLE,
  UNIQUE INDEX `code_UNIQUE` (`code` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `opc_p5_db`.`Brand`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `opc_p5_db`.`Brand` ;

CREATE TABLE IF NOT EXISTS `opc_p5_db`.`Brand` (
  `idBrand` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `code` VARCHAR(254) NOT NULL,
  `name` VARCHAR(1024) NOT NULL,
  `url` VARCHAR(1024) NOT NULL,
  `is_active` TINYINT NULL DEFAULT 1,
  PRIMARY KEY (`idBrand`),
  UNIQUE INDEX `idBrand_UNIQUE` (`idBrand` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `opc_p5_db`.`Product`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `opc_p5_db`.`Product` ;

CREATE TABLE IF NOT EXISTS `opc_p5_db`.`Product` (
  `idProduct` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `code` VARCHAR(254) NULL DEFAULT 'NoCode',
  `label` VARCHAR(1024) NULL DEFAULT 'Undefined Name',
  `url` VARCHAR(1024) NULL DEFAULT 'No Url',
  `is_active` TINYINT NULL DEFAULT 0,
  `ingredients_text` LONGTEXT NULL,
  `nutrition_grade_fr` VARCHAR(254) NULL,
  `quantity` VARCHAR(1024) NULL DEFAULT 'Undefined',
  PRIMARY KEY (`idProduct`),
  UNIQUE INDEX `idProduct_UNIQUE` (`idProduct` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `opc_p5_db`.`Product_has_Store`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `opc_p5_db`.`Product_has_Store` ;

CREATE TABLE IF NOT EXISTS `opc_p5_db`.`Product_has_Store` (
  `Product_idProduct` INT UNSIGNED NOT NULL,
  `Store_idStore` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`Product_idProduct`, `Store_idStore`),
  INDEX `fk_Product_has_Store_Store1_idx` (`Store_idStore` ASC) VISIBLE,
  INDEX `fk_Product_has_Store_Product1_idx` (`Product_idProduct` ASC) VISIBLE,
  CONSTRAINT `fk_Product_has_Store_Product1`
    FOREIGN KEY (`Product_idProduct`)
    REFERENCES `opc_p5_db`.`Product` (`idProduct`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Product_has_Store_Store1`
    FOREIGN KEY (`Store_idStore`)
    REFERENCES `opc_p5_db`.`Store` (`idStore`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `opc_p5_db`.`Category_has_Product`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `opc_p5_db`.`Category_has_Product` ;

CREATE TABLE IF NOT EXISTS `opc_p5_db`.`Category_has_Product` (
  `Product_idProduct` INT UNSIGNED NOT NULL,
  `Category_idCategory` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`Product_idProduct`, `Category_idCategory`),
  INDEX `fk_Category_has_Product_Product1_idx` (`Product_idProduct` ASC) VISIBLE,
  INDEX `fk_Category_has_Product_Category1_idx` (`Category_idCategory` ASC) VISIBLE,
  CONSTRAINT `fk_Category_has_Product_Category1`
    FOREIGN KEY (`Category_idCategory`)
    REFERENCES `opc_p5_db`.`Category` (`idCategory`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Category_has_Product_Product1`
    FOREIGN KEY (`Product_idProduct`)
    REFERENCES `opc_p5_db`.`Product` (`idProduct`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `opc_p5_db`.`Product_has_Brand`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `opc_p5_db`.`Product_has_Brand` ;

CREATE TABLE IF NOT EXISTS `opc_p5_db`.`Product_has_Brand` (
  `Product_idProduct` INT UNSIGNED NOT NULL,
  `Brand_idBrand` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`Product_idProduct`, `Brand_idBrand`),
  INDEX `fk_Product_has_Brand_Brand1_idx` (`Brand_idBrand` ASC) VISIBLE,
  INDEX `fk_Product_has_Brand_Product1_idx` (`Product_idProduct` ASC) VISIBLE,
  CONSTRAINT `fk_Product_has_Brand_Product1`
    FOREIGN KEY (`Product_idProduct`)
    REFERENCES `opc_p5_db`.`Product` (`idProduct`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Product_has_Brand_Brand1`
    FOREIGN KEY (`Brand_idBrand`)
    REFERENCES `opc_p5_db`.`Brand` (`idBrand`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `opc_p5_db`.`User`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `opc_p5_db`.`User` ;

CREATE TABLE IF NOT EXISTS `opc_p5_db`.`User` (
  `idUser` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(254) NULL,
  PRIMARY KEY (`idUser`),
  UNIQUE INDEX `idUser_UNIQUE` (`idUser` ASC) VISIBLE,
  UNIQUE INDEX `Name_UNIQUE` (`Name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `opc_p5_db`.`User Search`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `opc_p5_db`.`User Search` ;

CREATE TABLE IF NOT EXISTS `opc_p5_db`.`User Search` (
  `idSearch` INT NOT NULL,
  `Product_idProduct` INT UNSIGNED NOT NULL,
  `Category_idCategory` INT UNSIGNED NOT NULL,
  `User_idUser` INT UNSIGNED NOT NULL,
  `Created` DATE NOT NULL,
  PRIMARY KEY (`idSearch`),
  INDEX `fk_Product_has_Category_Category1_idx` (`Category_idCategory` ASC) VISIBLE,
  INDEX `fk_Product_has_Category_Product1_idx` (`Product_idProduct` ASC) VISIBLE,
  INDEX `fk_Product_has_Category_User1_idx` (`User_idUser` ASC) VISIBLE,
  CONSTRAINT `fk_Product_has_Category_Product1`
    FOREIGN KEY (`Product_idProduct`)
    REFERENCES `opc_p5_db`.`Product` (`idProduct`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Product_has_Category_Category1`
    FOREIGN KEY (`Category_idCategory`)
    REFERENCES `opc_p5_db`.`Category` (`idCategory`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Product_has_Category_User1`
    FOREIGN KEY (`User_idUser`)
    REFERENCES `opc_p5_db`.`User` (`idUser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
