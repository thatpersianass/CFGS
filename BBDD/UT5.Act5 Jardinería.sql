-- 1. Obtén un listado con el nombre de cada cliente y el nombre
-- y apellido de su representante de ventas.
SELECT C.nombre_cliente AS Nombre_Cliente, E.nombre AS Nombre_Empleado, E.apellido1 AS Apellido_Empleado
FROM cliente AS C
JOIN empleado AS E ON E.codigo_empleado = C.codigo_empleado_rep_ventas;

-- 2. Muestra el nombre de los clientes que no hayan realizado pagos junto con 
-- el nombre de sus representantes de ventas.
SELECT DISTINCT C.nombre_cliente AS Nombre_Cliente, E.nombre AS Nombre_Empleado, P.codigo_cliente AS Pago_realizado
FROM cliente AS C
JOIN empleado AS E ON E.codigo_empleado = C.codigo_empleado_rep_ventas
LEFT JOIN pago AS P ON C.codigo_cliente = P.codigo_cliente
WHERE P.codigo_cliente IS NULL;

-- 3. Devuelve el nombre de los clientes que no hayan hecho pagos y el nombre de sus
-- representantes junto con la ciudad de la oficina a la que pertenece el representante.
SELECT DISTINCT C.nombre_cliente AS Nombre_Cliente, E.nombre AS Nombre_Empleado, O.ciudad AS Ciudad_Empresa , P.codigo_cliente AS Pago_realizado
FROM cliente AS C
JOIN empleado AS E ON E.codigo_empleado = C.codigo_empleado_rep_ventas
JOIN oficina AS O ON O.codigo_oficina = E.codigo_oficina
LEFT JOIN pago AS P ON C.codigo_cliente = P.codigo_cliente
WHERE P.codigo_cliente IS NULL;

-- 4. Devuelve el nombre de los clientes y el nombre de sus representantes junto con la ciudad
-- de la oficina a la que pertenece el representante. 
SELECT C.nombre_cliente AS Nombre_Cliente, E.nombre AS Nombre_Empleado, O.ciudad AS Ciudad_Empresa
FROM cliente AS C
JOIN empleado AS E ON E.codigo_empleado = C.codigo_empleado_rep_ventas
JOIN oficina AS O ON O.codigo_oficina = E.codigo_oficina;

-- 5. Devuelve un listado de las diferentes gamas de producto que ha comprado cada cliente. 
SELECT DISTINCT C.nombre_cliente AS Cliente, PR.gama AS Gama
FROM cliente AS C
JOIN pedido AS P ON C.codigo_cliente = P.codigo_cliente
JOIN detalle_pedido AS DP ON P.codigo_pedido = DP.codigo_pedido
JOIN producto AS PR ON PR.codigo_producto = DP.codigo_producto;

-- 6. Devuelve un listado que muestre solamente los clientes que no han realizado ningún pedido.
SELECT DISTINCT C.nombre_cliente AS Cliente, P.codigo_cliente AS Pedido
FROM cliente AS C
LEFT JOIN pedido AS P ON P.codigo_cliente = C.codigo_cliente
WHERE P.codigo_cliente IS NULL;

-- 7. Devuelve un listado que muestre solamente los empleados que no tienen una oficina asociada. 
SELECT DISTINCT E.nombre AS Empleado, E.codigo_oficina AS Oficina
FROM empleado AS E
LEFT JOIN oficina AS O ON E.codigo_oficina = O.codigo_oficina
WHERE O.codigo_oficina IS NULL;

-- 8. Devuelve un listado de los productos que nunca han aparecido en un pedido. El resultado
-- debe mostrar el nombre, la descripción y la imagen del producto.
SELECT DISTINCT P.nombre AS Nombre_Producto, P.descripcion AS Descripcion, GM.imagen AS Imagen, DP.codigo_pedido AS Veces_Pedido
FROM producto P
JOIN gama_producto GM ON GM.gama = P.gama
LEFT JOIN detalle_pedido DP ON DP.codigo_producto = P.codigo_producto
WHERE DP.codigo_pedido IS NULL;

-- 9. Devuelve un listado con los clientes que han realizado algún pedido pero no han realizado ningún pago
SELECT DISTINCT C.nombre_cliente AS Cliente
FROM cliente C
JOIN pedido P ON C.codigo_cliente = P.codigo_cliente
LEFT JOIN pago PA ON C.codigo_cliente = PA.codigo_cliente
WHERE PA.codigo_cliente IS NULL;

-- 10. ¿Cuántos clientes existen con domicilio en la ciudad de Madrid? 
SELECT COUNT(*) AS Clientes_Madrid
FROM cliente C
WHERE C.ciudad = "Madrid";

-- 11. Calcula la fecha del primer y último pago realizado por cada uno de los clientes. El listado
-- deberá mostrar el nombre y los apellidos de cada cliente. 
SELECT  C.nombre_cliente AS Nombre,  MIN(P.fecha_pago) AS Primer_Pago,  MAX(P.fecha_pago) AS Ultimo_Pago
FROM  cliente C
JOIN  pago P ON C.codigo_cliente = P.codigo_cliente
GROUP BY  C.codigo_cliente, C.nombre_cliente;

-- 12.  La facturación que ha tenido la empresa en toda la historia, indicando la base imponible, el
-- IVA y el total facturado. La base imponible se calcula sumando el coste del producto por el
-- número de unidades vendidas de la tabla detalle_pedido. El IVA es el 21 % de la base
-- imponible, y el total la suma de los dos campos anteriores.
SELECT  SUM(DP.precio_unidad * DP.cantidad) AS Base_Imponible, SUM(DP.precio_unidad * DP.cantidad) * 0.21 AS IVA, SUM(DP.precio_unidad * DP.cantidad) * 1.21 AS Total_Facturado
FROM detalle_pedido DP;

-- 13. Devuelve el nombre del cliente con mayor límite de crédito
SELECT nombre_cliente, limite_credito
FROM cliente
WHERE limite_credito = (SELECT MAX(limite_credito) FROM cliente);

-- 14. Muestre la suma total de todos los pagos que se realizaron para cada uno de los años que parecen en la tabla pagos 
SELECT SUM(total) AS TOTAL, YEAR(fecha_pago) AS Anio
FROM pago
GROUP BY Anio;

-- 15. Devuelve el producto que más unidades tiene en stock
SELECT nombre, cantidad_en_stock
FROM producto
WHERE cantidad_en_stock = (SELECT MAX(cantidad_en_stock) FROM producto);

-- 16. Devuelve el listado de clientes indicando el nombre del cliente y cuántos pedidos ha realizado. Tenga en cuenta que pueden existir clientes que no han realizado ningún pedido. 
SELECT C.nombre_cliente AS Nombre, COUNT(P.codigo_pedido) AS Pedidos
FROM cliente C
JOIN pedido P ON C.codigo_cliente = P.codigo_cliente
GROUP BY  C.codigo_cliente, C.nombre_cliente;

-- 17. Devuelve el listado de clientes donde aparezca el nombre del cliente, el nombre y primer apellido de su representante de ventas y la ciudad donde está su oficina
SELECT C.nombre_cliente AS Nombre_Cliente, E.nombre AS Nombre_Empleado, E.apellido1 AS Apellido_Empleado, O.ciudad AS Ciudad
FROM cliente AS C
JOIN empleado AS E ON E.codigo_empleado = C.codigo_empleado_rep_ventas
JOIN oficina O ON E.codigo_oficina = O.codigo_oficina;

-- 18. Devuelve un listado de los productos que nunca han aparecido en un pedido
SELECT  P.nombre AS Nombre_Producto
FROM  producto P
LEFT JOIN  detalle_pedido DP ON P.codigo_producto = DP.codigo_producto
WHERE  DP.codigo_producto IS NULL;
