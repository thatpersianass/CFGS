CREATE SCHEMA IF NOT EXISTS pilotos DEFAULT CHARACTER SET latin1 COLLATE latin1_spanish_ci;
USE pilotos;

CREATE TABLE IF NOT EXISTS PILOTOS (
    Codigo VARCHAR(3) NOT NULL,
    Nombre VARCHAR(15) NOT NULL,
    Nacionalidad ENUM('Brasileña', 'Española', 'Inglesa', 'Alemana') NOT NULL,
    FechaNacimiento DATETIME NOT NULL,
    Debut YEAR NOT NULL CHECK(Debut BETWEEN 1990 AND 2020), 
    PRIMARY KEY (Codigo)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS CIRCUITOS (
    Nombre VARCHAR(15) NOT NULL,
    Pais VARCHAR(15) NOT NULL,
    Tipo VARCHAR(15) NOT NULL,
    Longitud DECIMAL(10, 1) NOT NULL CHECK(Longitud > 2400),
    Diseñador VARCHAR(20) NOT NULL,
    PRIMARY KEY (Nombre)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS CARRERAS (
    NombreGP VARCHAR(15) NOT NULL,
    Año YEAR NOT NULL CHECK(Año BETWEEN 2000 AND 2099), 
    FechaHoraInicio DATETIME NOT NULL, 
    NombreCircuito VARCHAR(15) NOT NULL,
    PRIMARY KEY (NombreGP, Año), 
    FOREIGN KEY (NombreCircuito) REFERENCES CIRCUITOS(Nombre)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS RESULTADOS (
    NombreGP VARCHAR(15) NOT NULL,
    Año YEAR NOT NULL,
    CodPiloto VARCHAR(3) NOT NULL,
    Puesto INT NOT NULL CHECK(Puesto BETWEEN 1 AND 99),
    PRIMARY KEY (NombreGP, Año, CodPiloto),
    FOREIGN KEY (NombreGP, Año) REFERENCES CARRERAS(NombreGP, Año), 
    FOREIGN KEY (CodPiloto) REFERENCES PILOTOS(Codigo)
) ENGINE=InnoDB;

-- Añadir una columna nueva a la tabla Circuitos que almacene el coste de la inscripción. Este coste supone un 60% de la longitud del circuito --
/*ALTER TABLE CIRCUITOS
ADD COLUMN CosteInscripcion DECIMAL(10,1);

UPDATE CIRCUITOS
SET CosteInscripcion = Longitud * 0.60;*/

-- Cambiar el nombre de la columna Año de la tabla Carreras por Anio --
/*ALTER TABLE CARRERAS
RENAME COLUMN `Año` TO `Anio`;*/

-- Establece una restricción para que las inserciones en la tabla Carreras sólo pueda aceptar valores en el campo FechaHoraInicio de las 13:00 a las 21:30 --
/*ALTER TABLE CARRERAS
ADD CONSTRAINT CHK_FechaHoraInicio CHECK (
    TIME(FechaHoraInicio) BETWEEN '13:00:00' AND '21:30:00'
);*/

-- Crea una vista que nos sirva para insertar datos en la tabla Carreras pero sólo para aquellas que correspondan al año 2022 --
/* CREATE VIEW VistaCarreras2022 AS
SELECT NombreGP, Año, FechaHoraInicio, NombreCircuito
FROM CARRERAS
WHERE Año = 2022
WITH CHECK OPTION; */

-- Crea una vista con los pilotos que hayan ganado más de una carrera en 2010, junto con el número de carreras ganadas --
/* vistacarreras2022CREATE VIEW VistaPilotosGanadores2010 AS
SELECT 
    p.Codigo,
    p.Nombre,
    COUNT(*) AS CarrerasGanadas
FROM RESULTADOS r
JOIN PILOTOS p ON r.CodPiloto = p.Codigo
WHERE r.Año = 2010
  AND r.Puesto = 1
GROUP BY p.Codigo, p.Nombre
HAVING COUNT(*) > 1; */
