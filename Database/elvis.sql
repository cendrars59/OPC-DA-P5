-- MySQL Script generated by MySQL Workbench
-- Thu Dec 26 23:24:01 2019
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Elvis
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Elvis
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Elvis` DEFAULT CHARACTER SET utf8 ;
USE `Elvis` ;

-- -----------------------------------------------------
-- Table `Elvis`.`Category`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Elvis`.`Category` ;

CREATE TABLE IF NOT EXISTS `Elvis`.`Category` (
  `idCategory` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `code` VARCHAR(254) NULL,
  `name` VARCHAR(1024) NULL,
  `url` VARCHAR(1024) NULL,
  `is_active` TINYINT NULL DEFAULT 0,
  PRIMARY KEY (`idCategory`),
  UNIQUE INDEX `idCategorie_UNIQUE` (`idCategory` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Elvis`.`Store`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Elvis`.`Store` ;

CREATE TABLE IF NOT EXISTS `Elvis`.`Store` (
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
-- Table `Elvis`.`Brand`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Elvis`.`Brand` ;

CREATE TABLE IF NOT EXISTS `Elvis`.`Brand` (
  `idBrand` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `code` VARCHAR(254) NOT NULL,
  `name` VARCHAR(1024) NOT NULL,
  `url` VARCHAR(1024) NOT NULL,
  `is_active` TINYINT NULL DEFAULT 1,
  PRIMARY KEY (`idBrand`),
  UNIQUE INDEX `idBrand_UNIQUE` (`idBrand` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Elvis`.`Product`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Elvis`.`Product` ;

CREATE TABLE IF NOT EXISTS `Elvis`.`Product` (
  `idProduct` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `code` VARCHAR(45) NULL DEFAULT 'NoCode',
  `label` VARCHAR(1024) NULL DEFAULT 'Undefined Name',
  `url` VARCHAR(1024) NULL DEFAULT 'No Url',
  `is_active` TINYINT NULL DEFAULT 0,
  PRIMARY KEY (`idProduct`),
  UNIQUE INDEX `idProduct_UNIQUE` (`idProduct` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Elvis`.`Product_has_Store`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Elvis`.`Product_has_Store` ;

CREATE TABLE IF NOT EXISTS `Elvis`.`Product_has_Store` (
  `Product_idProduct` INT UNSIGNED NOT NULL,
  `Store_idStore` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`Product_idProduct`, `Store_idStore`),
  INDEX `fk_Product_has_Store_Store1_idx` (`Store_idStore` ASC) VISIBLE,
  INDEX `fk_Product_has_Store_Product1_idx` (`Product_idProduct` ASC) VISIBLE,
  CONSTRAINT `fk_Product_has_Store_Product1`
    FOREIGN KEY (`Product_idProduct`)
    REFERENCES `Elvis`.`Product` (`idProduct`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Product_has_Store_Store1`
    FOREIGN KEY (`Store_idStore`)
    REFERENCES `Elvis`.`Store` (`idStore`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Elvis`.`Category_has_Product`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Elvis`.`Category_has_Product` ;

CREATE TABLE IF NOT EXISTS `Elvis`.`Category_has_Product` (
  `Product_idProduct` INT UNSIGNED NOT NULL,
  `Category_idCategory` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`Product_idProduct`, `Category_idCategory`),
  INDEX `fk_Category_has_Product_Product1_idx` (`Product_idProduct` ASC) VISIBLE,
  INDEX `fk_Category_has_Product_Category1_idx` (`Category_idCategory` ASC) VISIBLE,
  CONSTRAINT `fk_Category_has_Product_Category1`
    FOREIGN KEY (`Category_idCategory`)
    REFERENCES `Elvis`.`Category` (`idCategory`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Category_has_Product_Product1`
    FOREIGN KEY (`Product_idProduct`)
    REFERENCES `Elvis`.`Product` (`idProduct`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Elvis`.`Product_has_Brand`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Elvis`.`Product_has_Brand` ;

CREATE TABLE IF NOT EXISTS `Elvis`.`Product_has_Brand` (
  `Product_idProduct` INT UNSIGNED NOT NULL,
  `Brand_idBrand` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`Product_idProduct`, `Brand_idBrand`),
  INDEX `fk_Product_has_Brand_Brand1_idx` (`Brand_idBrand` ASC) VISIBLE,
  INDEX `fk_Product_has_Brand_Product1_idx` (`Product_idProduct` ASC) VISIBLE,
  CONSTRAINT `fk_Product_has_Brand_Product1`
    FOREIGN KEY (`Product_idProduct`)
    REFERENCES `Elvis`.`Product` (`idProduct`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Product_has_Brand_Brand1`
    FOREIGN KEY (`Brand_idBrand`)
    REFERENCES `Elvis`.`Brand` (`idBrand`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Elvis`.`User`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Elvis`.`User` ;

CREATE TABLE IF NOT EXISTS `Elvis`.`User` (
  `idUser` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(254) NULL,
  PRIMARY KEY (`idUser`),
  UNIQUE INDEX `idUser_UNIQUE` (`idUser` ASC) VISIBLE,
  UNIQUE INDEX `Name_UNIQUE` (`Name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Elvis`.`User Search`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Elvis`.`User Search` ;

CREATE TABLE IF NOT EXISTS `Elvis`.`User Search` (
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
    REFERENCES `Elvis`.`Product` (`idProduct`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Product_has_Category_Category1`
    FOREIGN KEY (`Category_idCategory`)
    REFERENCES `Elvis`.`Category` (`idCategory`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Product_has_Category_User1`
    FOREIGN KEY (`User_idUser`)
    REFERENCES `Elvis`.`User` (`idUser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
