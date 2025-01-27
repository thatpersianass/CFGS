/* 1. Realiza una transacción para insertar una nueva oficina en Almería, un empleado
en dicha oficina que sea representante de ventas y un cliente que tenga como
representante de ventas el empleado que hemos creado en el paso anterior.
Establece un savepoint en la primera inserción al que se pueda volver si falla la
inserción del empleado*/
-- Revertir los cambios realizados en la transacción
START TRANSACTION;
DELETE FROM cliente WHERE codigo_empleado_rep_ventas IN (SELECT codigo_empleado FROM empleado WHERE codigo_oficina = 'ALM-ES');
DELETE FROM empleado WHERE codigo_oficina = 'ALM-ES';
DELETE FROM oficina WHERE codigo_oficina = 'ALM-ES';
COMMIT;

START TRANSACTION;
INSERT INTO oficina(codigo_oficina, ciudad, pais, region, telefono, codigo_postal, linea_direccion1, fax)
VALUES ('ALM-ES', 'Almería', 'España', 'Europa', 950123456, 32781, 'Calle desvivicion', NULL);
SAVEPOINT oficina;
INSERT INTO empleado(codigo_empleado, nombre, apellido1, apellido2, extension, email, codigo_oficina, codigo_jefe, puesto, fax)
VALUES (1001, 'Carlos', 'Lopez', 'Cortéz', 5748, 'carloslopez@almeria.es', 'ALM-ES', NULL, 'Representante de ventas', NULL);
SAVEPOINT empleado;
INSERT INTO cliente(codigo_cliente, nombre_cliente, nombre_contacto, apellido_contacto, telefono, linea_direccion1, ciudad, region, pais, codigo_postal, codigo_empleado_rep_ventas, fax)
VALUES (5001, 'Frutas MJ', 'Camilo', 'Jiemenez', 8738738, 'Calle Pingüino Cojo, 132', 'Almería', 'Europa', 'España', NULL, 1001, NULL);
COMMIT;
