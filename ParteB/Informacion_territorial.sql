CREATE DATABASE IF NOT EXISTS `Informacion_territorial`;

USE Informacion_territorial;

DROP TABLE IF EXISTS `Pais`;

CREATE TABLE Pais(
    `Nombre_Pais`    VARCHAR(100) NOT NULL,
    `Continente`      VARCHAR(100) NOT NULL,
    `Nombre_Capital`  VARCHAR(100) NOT NULL,
    PRIMARY KEY (`Nombre_pais`)
);

DROP TABLE IF EXISTS `Region`;

CREATE TABLE Region(
    `ID_R`        VARCHAR(50) NOT NULL,
    `Cantidad_C`  INT NOT NULL,
    `Nombre_CP`   VARCHAR(50) NOT NULL,
    `Nombre_R`    VARCHAR(100) NOT NULL,
    PRIMARY KEY (`ID_R`)
);

DROP TABLE IF EXISTS `Salud`;

CREATE TABLE Salud(
    ID_Establecimiento          INT  NOT NULL,
    N_Establecimiento           VARCHAR(200) NOT NULL,
    Telefono_Establecimiento    VARCHAR(20) NOT NULL,
    PRIMARY KEY (`ID_Establecimiento`)
);

DROP TABLE IF EXISTS `Comuna`;

CREATE TABLE Comuna(
    `ID_C`        INT          NOT NULL,
    `Nombre_P`    VARCHAR(100) NOT NULL,
    `PoblacionT`  INT          NOT NULL,
    `Nombre_C`    VARCHAR(100) NOT NULL,
    PRIMARY KEY (`ID_C`),
    CONSTRAINT `Comuna_ibfk_1` FOREIGN KEY (`ID_Establecimiento`) REFERENCES `Salud` (`ID_Establecimiento`),
    CONSTRAINT `Comuna_ibfk_2` FOREIGN KEY (`ID_Tipo_Ocupación`) REFERENCES `Trabajo`(`ID_Tipo_Ocupación`),
    CONSTRAINT `Comuna_ibfk_3` FOREIGN KEY (`ID_Antena`) REFERENCES `Conectividad` (`ID_Antena`),
    CONSTRAINT `Comuna_ibfk_4` FOREIGN KEY (`ID_Estadio`) REFERENCES `Entretención`(`ID_Estadio`)
);



DROP TABLE IF EXISTS `Trabajo`;

CREATE TABLE Trabajo(
    ID_Tipo_Ocupación       INT NOT NULL,
    H_ParaTrabajar          INT NOT NULL,
    M_ParaTrabajar          INT NOT NULL,
    H_Desocupados           INT NOT NULL,
    M_Desocupadas           INT NOT NULL,
    H_Ocupados              INT NOT NULL,
    M_Ocupadas              INT NOT NULL,
    PRIMARY KEY (`ID_Tipo_Ocupación`)
);

DROP TABLE IF EXISTS `Conectividad`;

CREATE TABLE Conectividad(
    ID_Antena       INT NOT NULL,
    Total_Antenas   INT NOT NULL,
    N_Empresa       VARCHAR(200) NOT NULL,
    PRIMARY KEY (`ID_Antena`)
);