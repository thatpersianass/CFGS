CREATE USER santiago IDENTIFIED BY '12345';
CREATE USER felipe IDENTIFIED BY '12345';
CREATE USER auxiliar IDENTIFIED BY '12345';

GRANT INSERT, DELETE ON pilotos.* TO santiago;

GRANT SELECT, INSERT, UPDATE ON pilotos.Carreras TO felipe;
GRANT SELECT, INSERT, UPDATE ON pilotos.Resultados TO felipe;

SHOW GRANTS FOR santiago;
SHOW GRANTS FOR felipe;

CREATE VIEW pilotos.vista_circuitos AS 
SELECT Nombre, País, Tipo FROM pilotos.Circuitos;

GRANT SELECT ON pilotos.vista_circuitos TO auxiliar;

ALTER USER santiago IDENTIFIED BY 'xxx333';
