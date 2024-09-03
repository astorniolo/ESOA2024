-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema banko
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema banko
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `banko` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `banko` ;

-- -----------------------------------------------------
-- Table `banko`.`cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `banko`.`cliente` (
  `idCliente` INT NOT NULL,
  `clienteNombre` VARCHAR(45) NULL DEFAULT NULL,
  `clienteDomicilio` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idCliente`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `banko`.`cuenta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `banko`.`cuenta` (
  `idCuenta` INT NOT NULL,
  `nombreSucursal` VARCHAR(50) CHARACTER SET 'utf8mb3' NULL DEFAULT NULL,
  `saldo` FLOAT NULL DEFAULT NULL,
  `cliente_idCliente` INT NOT NULL,
  PRIMARY KEY (`idCuenta`, `cliente_idCliente`),
  INDEX `fk_cuenta_cliente1_idx` (`cliente_idCliente` ASC) VISIBLE,
  CONSTRAINT `fk_cuenta_cliente1`
    FOREIGN KEY (`cliente_idCliente`)
    REFERENCES `banko`.`cliente` (`idCliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `banko`.`prestamo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `banko`.`prestamo` (
  `idPrestamo` INT NOT NULL,
  `nombreSucursal` VARCHAR(50) CHARACTER SET 'utf8mb3' NULL DEFAULT NULL,
  `Importe` FLOAT NULL DEFAULT NULL,
  `cliente_idCliente` INT NOT NULL,
  PRIMARY KEY (`idPrestamo`, `cliente_idCliente`),
  INDEX `fk_prestamo_cliente_idx` (`cliente_idCliente` ASC) VISIBLE,
  CONSTRAINT `fk_prestamo_cliente`
    FOREIGN KEY (`cliente_idCliente`)
    REFERENCES `banko`.`cliente` (`idCliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `banko`.`sucursal`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `banko`.`sucursal` (
  `idSucursal` INT NOT NULL,
  `ciudadSucursal` VARCHAR(50) CHARACTER SET 'utf8mb3' NULL DEFAULT NULL,
  `activos` FLOAT NULL DEFAULT NULL,
  `cliente_idCliente` INT NOT NULL,
  PRIMARY KEY (`idSucursal`),
  INDEX `fk_sucursal_cliente1_idx` (`cliente_idCliente` ASC) VISIBLE,
  CONSTRAINT `fk_sucursal_cliente1`
    FOREIGN KEY (`cliente_idCliente`)
    REFERENCES `banko`.`cliente` (`idCliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;