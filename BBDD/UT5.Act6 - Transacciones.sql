/* 1. Realiza una transacción para insertar una nueva oficina en Almería, un empleado
en dicha oficina que sea representante de ventas y un cliente que tenga como
representante de ventas el empleado que hemos creado en el paso anterior.
Establece un savepoint en la primera inserción al que se pueda volver si falla la
inserción del empleado*/

/* -- Revertir los cambios realizados en la transacción
START TRANSACTION;
DELETE FROM cliente WHERE codigo_empleado_rep_ventas IN (SELECT codigo_empleado FROM empleado WHERE codigo_oficina = 'ALM-ES');
DELETE FROM empleado WHERE codigo_oficina = 'ALM-ES';
DELETE FROM oficina WHERE codigo_oficina = 'ALM-ES';
COMMIT; */

/* START TRANSACTION;
INSERT INTO oficina(codigo_oficina, ciudad, pais, region, telefono, codigo_postal, linea_direccion1)
VALUES ('ALM-ES', 'Almería', 'España', 'Europa', 950123456, 32781, 'Calle desvivicion');
SAVEPOINT oficina;
INSERT INTO empleado(codigo_empleado, nombre, apellido1, apellido2, extension, email, codigo_oficina, codigo_jefe, puesto)
VALUES (1001, 'Carlos', 'Lopez', 'Cortéz', 5748, 'carloslopez@almeria.es', 'ALM-ES', NULL, 'Representante de ventas');
SAVEPOINT empleado;
INSERT INTO cliente(codigo_cliente, nombre_cliente, nombre_contacto, apellido_contacto, telefono, linea_direccion1, ciudad, region, pais, codigo_postal, codigo_empleado_rep_ventas,fax)
VALUES (5001, 'Frutas MJ', 'Camilo', 'Jiemenez', 8738738, 'Calle Pingüino Cojo, 132', 'Almería', 'Europa', 'España', NULL, 1001,23382);
COMMIT;

DESCRIBE oficina;
DESCRIBE empleado;
DESCRIBE cliente; */

/* 2. Realiza una transacción que inserte un pedido para el cliente que acabamos de
crear, que contenga al menos dos productos diferentes y que actualice el código
del cliente que hemos creado en el paso anterior. Averigua si hubo cambios en las
tablas relacionadas y si crees conveniente establecer algún savepoint o algún
rollback. */

/* START TRANSACTION;

INSERT INTO oficina(codigo_oficina, ciudad, pais, region, telefono, codigo_postal, linea_direccion1)
SELECT 'ALM-ES', 'Almería', 'España', 'Europa', 950123456, 32781, 'Calle desvivicion'
FROM DUAL
WHERE NOT EXISTS (
    SELECT 1 FROM oficina WHERE codigo_oficina = 'ALM-ES'
);
SAVEPOINT oficina_insertada;

UPDATE cliente
SET codigo_cliente = 5002
WHERE codigo_cliente = 5001;
SAVEPOINT cliente_actualizado;

INSERT INTO pedido(codigo_pedido, codigo_cliente, fecha_pedido, fecha_esperada, estado)
VALUES (1001, 5002, CURDATE(), DATE_ADD(CURDATE(), INTERVAL 7 DAY), 'En proceso');
SAVEPOINT pedido_insertado;

INSERT INTO detalle_pedido(codigo_pedido, codigo_producto, cantidad, precio_unidad, numero_linea)
VALUES (1001, 2001, 5, 15.50, 3),
       (1001, 2002, 3, 25.75, 9);
SAVEPOINT detalles_insertados;

COMMIT;

ROLLBACK TO oficina_insertada; */



/* 3. Borra el cliente y averigua si hubo cambios en las tablas relacionadas */

/* START TRANSACTION;
DELETE FROM cliente WHERE codigo_empleado_rep_ventas IN (SELECT codigo_empleado FROM empleado WHERE codigo_oficina = 'ALM-ES');
DELETE FROM empleado WHERE codigo_oficina = 'ALM-ES';
DELETE FROM oficina WHERE codigo_oficina = 'ALM-ES';
COMMIT; */


/* 4. Realiza una transacción que elimine los clientes que no hayan realizado ningún
pedido e incrementa en un 20% el precio de los productos que no tengan pedidos */

/* START TRANSACTION;

DELETE FROM cliente
WHERE codigo_cliente NOT IN (SELECT DISTINCT codigo_cliente FROM pedido);

UPDATE producto
SET precio_venta = precio_venta * 1.20
WHERE codigo_producto NOT IN (SELECT DISTINCT codigo_producto FROM detalle_pedido);

COMMIT; */


/* 5. Borra los pagos del cliente con menor límite de crédito. */
/* START TRANSACTION;

DELETE FROM pago
WHERE codigo_cliente = (
    SELECT codigo_cliente
    FROM cliente
    ORDER BY limite_credito ASC
    LIMIT 1
);

COMMIT;*/

/* 6. Establece a 0 el límite de crédito del cliente que menos unidades pedidas tenga
del producto 11679. */

/* START TRANSACTION;

UPDATE cliente
SET limite_credito = 0
WHERE codigo_cliente = (
    SELECT codigo_cliente
    FROM detalle_pedido dp
    JOIN pedido p ON dp.codigo_pedido = p.codigo_pedido
    WHERE dp.codigo_producto = 11679
    GROUP BY codigo_cliente
    ORDER BY SUM(dp.cantidad) ASC
    LIMIT 1
);

COMMIT; */


/* 7. Modifica la tabla detalle_pedido para insertar un campo numérico llamado iva.
Mediante una transacción, establece el valor de ese campo a 18 para aquellos
registros cuyo pedido tenga fecha a partir de Enero de 2009. A continuación
actualiza el resto de pedidos estableciendo el iva al 21. */

/* START TRANSACTION;

ALTER TABLE detalle_pedido
ADD COLUMN iva DECIMAL(5,2);

UPDATE detalle_pedido
SET iva = 18
WHERE codigo_pedido IN (
    SELECT codigo_pedido
    FROM pedido
    WHERE fecha_pedido >= '2009-01-01'
);

UPDATE detalle_pedido
SET iva = 21
WHERE codigo_pedido NOT IN (
    SELECT codigo_pedido
    FROM pedido
    WHERE fecha_pedido >= '2009-01-01'
);

COMMIT; */

/* 8. Modifica la tabla detalle_pedido para incorporar un campo numérico llamado
total_linea y actualiza todos sus registros para calcular su valor con la fórmula:
total_linea = precio_unidad*cantidad * (1 + (iva/100)); */

/* START TRANSACTION;

ALTER TABLE detalle_pedido
ADD COLUMN total_linea DECIMAL(10,2);

UPDATE detalle_pedido
SET total_linea = precio_unidad * cantidad * (1 + (iva / 100));

COMMIT; */


/* 9. Borra el cliente que menor límite de crédito tenga. ¿Es posible borrarlo solo con
una consulta? ¿Por qué? */

/* START TRANSACTION;

DELETE FROM cliente
WHERE codigo_cliente = (
    SELECT codigo_cliente
    FROM cliente
    ORDER BY limite_credito ASC
    LIMIT 1
);

COMMIT; */

/* No es posible borrar directamente al cliente con el menor límite de crédito si tiene registros relacionados en otras tablas debido a las restricciones 
de integridad referencial. Estas restricciones aseguran que no se eliminen registros de una tabla si existen datos dependientes en otras tablas, 
como pedidos o pagos asociados al cliente. */


/* 10.Mediante una transacción inserta una oficina con sede en Granada y tres
empleados que sean representantes de ventas. Inserta tres clientes que tengan
como representantes de ventas los empleados que hemos creado en el paso
anterior. */

/* START TRANSACTION;

INSERT INTO oficina(codigo_oficina, ciudad, pais, region, telefono, codigo_postal, linea_direccion1)
VALUES ('GRD-ES', 'Granada', 'España', 'Europa', 958123456, 18001, 'Calle Granadera 12');

INSERT INTO empleado(codigo_empleado, nombre, apellido1, apellido2, extension, email, codigo_oficina, puesto)
VALUES 
(2001, 'Ana', 'Gomez', 'Perez', 1234, 'ana.gomez@granada.es', 'GRD-ES', 'Representante de ventas'),
(2002, 'Luis', 'Rodriguez', 'Martinez', 1235, 'luis.rodriguez@granada.es', 'GRD-ES', 'Representante de ventas'),
(2003, 'Carlos', 'Jimenez', 'Lopez', 1236, 'carlos.jimenez@granada.es', 'GRD-ES', 'Representante de ventas');

INSERT INTO cliente(codigo_cliente, nombre_cliente, nombre_contacto, apellido_contacto, telefono, linea_direccion1, ciudad, region, pais, codigo_postal, codigo_empleado_rep_ventas)
VALUES 
(6001, 'Jardines y Flores', 'Sara', 'Vazquez', 958654321, 'Avenida de la Alhambra 15', 'Granada', 'Europa', 'España', 18001, 2001),
(6002, 'Frutas Granada', 'Miguel', 'Cruz', 958654322, 'Calle Real 25', 'Granada', 'Europa', 'España', 18001, 2002),
(6003, 'Distribuciones Luis', 'Raul', 'Torres', 958654323, 'Calle de la Vega 30', 'Granada', 'Europa', 'España', 18001, 2003);

COMMIT; */

/* 11.Realiza una transacción que inserte un pedido para cada uno de los clientes. Cada
pedido debe incluir dos productos. */

/* START TRANSACTION;

INSERT INTO pedido(codigo_pedido, codigo_cliente, fecha_pedido, fecha_esperada, estado)
VALUES 
(1001, 6001, CURDATE(), DATE_ADD(CURDATE(), INTERVAL 7 DAY), 'En proceso'),
(1002, 6002, CURDATE(), DATE_ADD(CURDATE(), INTERVAL 7 DAY), 'En proceso'),
(1003, 6003, CURDATE(), DATE_ADD(CURDATE(), INTERVAL 7 DAY), 'En proceso');

INSERT INTO detalle_pedido(codigo_pedido, codigo_producto, cantidad, precio_unidad)
VALUES 
(1001, 2001, 5, 15.50),
(1001, 2002, 3, 25.75),
(1002, 2001, 4, 15.50),
(1002, 2002, 6, 25.75),
(1003, 2001, 7, 15.50),
(1003, 2002, 2, 25.75);

COMMIT; */

/* 12.Borra uno de los clientes y comprueba si hubo cambios en las tablas relacionadas.
Si no hubo cambios, modifica las tablas necesarias estableciendo la clave foránea
con la cláusula ON DELETE CASCADE. */

/* START TRANSACTION;

DELETE FROM cliente WHERE codigo_cliente = 6001;

COMMIT;

START TRANSACTION;
ALTER TABLE pedido
DROP FOREIGN KEY pedido_ibfk_1,
ADD CONSTRAINT pedido_ibfk_1 FOREIGN KEY (codigo_cliente) REFERENCES cliente(codigo_cliente) ON DELETE CASCADE;
COMMIT;

START TRANSACTION;
ALTER TABLE detalle_pedido
DROP FOREIGN KEY detalle_pedido_ibfk_1, 
ADD CONSTRAINT detalle_pedido_ibfk_1 FOREIGN KEY (codigo_pedido) REFERENCES pedido(codigo_pedido) ON DELETE CASCADE;
COMMIT;

START TRANSACTION;
ALTER TABLE empleado
DROP FOREIGN KEY empleado_ibfk_1,  -- El nombre de la clave foránea puede variar
ADD CONSTRAINT empleado_ibfk_1 FOREIGN KEY (codigo_oficina) REFERENCES oficina(codigo_oficina) ON DELETE CASCADE;
COMMIT;

START TRANSACTION;

DELETE FROM cliente WHERE codigo_cliente = 6001;

COMMIT; */

/* 13.Realiza una transacción que realice los pagos de los pedidos que han realizado los
clientes del ejercicio anterior. */

/* START TRANSACTION;

INSERT INTO pago(codigo_cliente, total, fecha_pago)
SELECT 
    p.codigo_cliente,
    dp.cantidad * dp.precio_unidad,
    CURDATE()
FROM pedido p
JOIN detalle_pedido dp ON p.codigo_pedido = dp.codigo_pedido
WHERE p.codigo_cliente IN (6001, 6002, 6003);

COMMIT; */