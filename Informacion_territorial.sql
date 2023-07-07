CREATE DATABASE IF NOT EXISTS `Informacion_territorial`;

USE Informacion_territorial;

DROP TABLE IF EXISTS `Pais`;
CREATE TABLE Pais(
    `Nombre_Pais`     VARCHAR(100) NOT NULL,
    `Continente`      VARCHAR(100) NOT NULL,
    `Nombre_Capital`  VARCHAR(100) NOT NULL,
    PRIMARY KEY (`Nombre_pais`)
);

INSERT INTO Pais (Nombre_Pais, Continente, Nombre_Capital) VALUES ('Chile', 'America del Sur', 'Santiago');

DROP TABLE IF EXISTS `Region`;
CREATE TABLE Region(
    `ID_R`        VARCHAR(50)  NOT NULL,
    `Cantidad_C`  INT          NOT NULL,
    `Nombre_CP`   VARCHAR(50)  NOT NULL,
    `Nombre_R`    VARCHAR(100) NOT NULL,
    `Nombre_Pais` VARCHAR(100) NOT NULL,
    PRIMARY KEY (`ID_R`),
    FOREIGN KEY (Nombre_Pais) REFERENCES Pais (Nombre_Pais)
);


DROP TABLE IF EXISTS `Comuna`;
CREATE TABLE Comuna(
    `ID_C`        INT          NOT NULL,
    `Nombre_P`    VARCHAR(100) NOT NULL,
    `PoblacionT`  INT          NOT NULL,
    `Nombre_C`    VARCHAR(100) NOT NULL,
    `Superficie_C` VARCHAR(20) NOT NULL,
    `Densidad_C`  VARCHAR(20) NOT NULL,
    `ID_R`        VARCHAR(100) NOT NULL,
    PRIMARY KEY (`ID_C`),
    FOREIGN KEY (ID_R) REFERENCES Region (ID_R)
);

DROP TABLE IF EXISTS `Salud`;
CREATE TABLE Salud(
    ID_Establecimiento          INT NOT NULL,
    N_Establecimiento           VARCHAR(200) NOT NULL,
    Telefono_Establecimiento    VARCHAR(20) NOT NULL,
    ID_C                        INT NOT NULL,
    PRIMARY KEY (`ID_Establecimiento`),
    FOREIGN KEY (ID_C) REFERENCES Comuna (ID_C)
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
    ID_C                    INT NOT NULL,
    PRIMARY KEY (`ID_Tipo_Ocupación`),
    FOREIGN KEY (ID_C) REFERENCES Comuna (ID_C)
);

DROP TABLE IF EXISTS `Seguridad`;
CREATE TABLE Seguridad(
    ID_Establecimientos   INT NOT NULL,
    Comisarias            INT NOT NULL,
    Reten                 INT NOT NULL,
    Subcomisaria          INT NOT NULL,
    Prefactura            INT NOT NULL,
    Tenencia              INT NOT NULL,
    Zona                  INT NOT NULL,
    ID_C                  INT NOT NULL,
    PRIMARY KEY (`ID_Establecimientos`),
    FOREIGN KEY (ID_C) REFERENCES Comuna (ID_C)
);

DROP TABLE IF EXISTS `Entretencion`;
CREATE TABLE Entretencion(
    ID_Estadio          INT          NOT NULL,
    Nombre_Estadio      VARCHAR(200) NULL,
    Ano_Apertura        INT          NOT NULL,
    Equipos_Locales     VARCHAR(200) NOT NULL,
    Capacidad_Estadio   INT          NOT NULL,
    ID_C                INT          NOT NULL,
    PRIMARY KEY (`ID_Estadio`),
    FOREIGN KEY (ID_C) REFERENCES Comuna (ID_C)
);

DROP TABLE IF EXISTS `Bienestar`;
CREATE TABLE Bienestar(
    ID_Bienestar        INT          NOT NULL,
    P_Salud             INT          NOT NULL,
    P_Seguridad         INT          NOT NULL,
    P_Trabajo           INT          NOT NULL,
    P_Entretencion      INT          NOT NULL,
    Total               INT          NOT NULL,
    ID_C                INT          NOT NULL,
    PRIMARY KEY (`ID_Bienestar`),
    FOREIGN KEY (ID_C) REFERENCES Comuna (ID_C)
);





