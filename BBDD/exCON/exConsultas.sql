/* Muestra el listado de las categorías que tienen asociados más de 4 productos. La
salida de la consulta debe mostrar el nombre de la categoría y el número de productos
asociados */
SELECT C.nombre AS Categoria, COUNT(P.id) AS nro_productos
FROM categorias C
JOIN productos P ON P.categoria_id = C.id
GROUP BY C.id
HAVING COUNT(P.id) >= 4; -- LISTO

/* Muestra el listado de clientes que aún no han saldado el importe de alguno de los
pedidos que haya realizado */
SELECT DISTINCT U.nombre AS Nombre_Cliente, PE.id AS ID_Pedido
FROM usuarios U
JOIN pedidos PE ON PE.usuario_id = U.id
LEFT JOIN pagos PA ON PA.pedido_id = PE.id
WHERE PA.pedido_id IS NULL; -- LISTO

/* Muestra la calificación promedio de cada producto que haya tenido reseñas. La
salida debe mostrar el nombre del producto, la calificación promedio y el total de
reseñas. Ordena la salida */
SELECT P.nombre AS Nombre_producto, AVG(O.calificacion) AS Promedio, COUNT(O.comentario) AS nro_reseñas
FROM productos P
JOIN opiniones O ON O.producto_id = P.id
GROUP BY P.id, O.producto_id; -- LISTO

/* Muestra los clientes que han pedido más de 10 productos en total. La salida debe
mostrar el nombre del cliente y el número de pedidos. */
SELECT U.nombre AS Cliente, count(P.id) AS nro_pedidos
FROM usuarios U
JOIN pedidos P ON P.usuario_id = U.id
JOIN detalles_pedido D ON D.pedido_id = P.id
GROUP BY U.id
HAVING COUNT(D.producto_id) >= 10; -- LISTO

/* Muestra el cliente que ha realizado el mayor pago en el año 2025. La salida debe
mostrar el/los nombre/s del/los cliente/s y el importe abonado */
SELECT U.nombre AS Cliente, PA.pago AS importe_abonado, PA.fecha_pago
FROM usuarios U
JOIN pedidos PE ON PE.usuario_id = U.id
JOIN pagos PA ON PA.pedido_id = PE.id
WHERE 2025-01-01 <= PA.fecha_pago <= 2025-12-31 AND PA.pago = (SELECT MAX(pago) FROM pagos); -- LISTO

/* Mostrar el precio medio de los productos que cuentan con reseñas valoradas con 4
estrellas o más */
SELECT P.nombre AS nombre_producto, AVG(P.precio) AS Promedio_precio
FROM productos P
JOIN opiniones O ON O.producto_id = P.id
WHERE O.calificacion >= 4
GROUP BY P.id; -- LISTO

/* Actualiza el stock de los productos que no han sido pedidos por ningún cliente a 0,
siempre y cuando pertenezcan a la categoría impresoras o laptops */
/* UPDATE productos
SET stock = 0
WHERE (
	SELECT D.producto_id FROM productos P
    LEFT JOIN detalles_pedido D ON D.producto_id = P.id
) IS NULL; */

/* Muestra los pedidos que tengan más de 3 productos y el precio medio de los
mismos. La salida debe mostrar el id del pedido, la cantidad de productos en dicho
pedido, y el precio medio del mismo */
SELECT PE.id AS NRO_pedido, COUNT(D.producto_id) AS cantidad_productos, AVG(PR.precio) AS promedio_precio
FROM pedidos PE
JOIN detalles_pedido D ON D.pedido_id = PE.id
JOIN productos PR ON D.producto_id = PR.id
GROUP BY PE.id
HAVING COUNT(D.producto_id) >= 3; -- LISTO

/*  Muestra el producto más vendido */
SELECT P.nombre AS nombre_producto, COUNT(D.producto_id) AS nro_veces_pedido
FROM productos P
JOIN detalles_pedido D ON P.id = D.producto_id
GROUP BY P.id
ORDER BY COUNT(D.producto_id) DESC
LIMIT 1; -- LISTO

/* Borra los clientes que no han realizado ningún pedido o, si han realizado pedidos, la
suma total del precio de todos ellos es inferior a 100 */
/* DELETE FROM usuarios
WHERE (
	SELECT DISTINCT U.id FROM usuarios U
	LEFT JOIN pedidos P ON P.usuario_id = u.id
	WHERE P.id IS NULL
); */