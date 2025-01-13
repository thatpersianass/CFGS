-- 1. Obtener el código y el tipo de las pistas de tenis que están operativas --
SELECT codigo, tipo
FROM pistas P JOIN pistas_abiertas PA
ON P.id = PA.id_pista
WHERE P.tipo LIKE "tenis" AND PA.operativa = 1;

-- 2. Obtener el código y el tipo de las pistas de los polideportivos de Zaragoza --
SELECT codigo, tipo
FROM pistas P JOIN polideportivos polideportivos
ON P.id_polideportivo = polideportivos.id
WHERE polideportivos.ciudad LIKE "Zaragoza";

-- 3. Precio medio, por tipo de pista, de las pistas que no están operativas --
SELECT AVG(Precio) AS precio_medio, tipo
FROM pistas P JOIN pistas_abiertas PA
ON P.id = PA.id_pista
WHERE PA.operativa = 0
GROUP BY P.tipo;

-- 4. Cantidad de pistas que hay en cada polideportivo --
SELECT polideportivos.nombre, COUNT(*) AS cantidad_pistas
FROM pistas P JOIN polideportivos polideportivos
ON P.id_polideportivo = polideportivos.id
GROUP BY polideportivos.nombre;

-- 5. Nº de reservas que ha hecho cada usuario. Ordena la salida por el campo apellido --
SELECT UR.id_usuario, COUNT(*) AS num_reservas
FROM usuario_reserva UR
JOIN reservas R ON UR.id_reserva = R.id
JOIN usuarios U ON UR.id_usuario = U.id
GROUP BY UR.id_usuario
ORDER BY U.apellidos;

-- 6. Número de pistas que hay de cada tipo en el polideportivo 'ACTUR 1' --
SELECT P.tipo, COUNT(*) AS cantidad_pistas
FROM pistas P
JOIN polideportivos PO ON P.id_polideportivo = PO.id
WHERE PO.nombre = 'ACTUR 1'
GROUP BY P.tipo;

-- 7. Mostrar, para cada polideportivo, el código y tipo de las pistas que tiene --
SELECT PO.nombre AS polideportivo, P.codigo, P.tipo
FROM polideportivos PO
JOIN pistas P ON PO.id = P.id_polideportivo;

-- 8. Mostrar, para cada pista, el código de reserva que ha tenido. Si nunca se ha reservado, se --
-- mostrarán sólo sus datos. (Puede ocurrir que una pista no esté relacionada con ninguna reserva). --
SELECT P.codigo AS pista_codigo, R.id AS reserva_codigo
FROM pistas P
LEFT JOIN reservas R ON P.id = R.id_pista;

-- 9. Mostrar cuántas veces se ha reservado cada pista --
SELECT P.id AS pista_id, COUNT(R.id) AS veces_reservada
FROM pistas P
LEFT JOIN reservas R ON P.id = R.id_pista
GROUP BY P.codigo;

-- 10. Mostrar cuántas reservas ha hecho cada usuario. Puede ocurrir que exista algún usuario que no haya hecho reservas --
SELECT U.id, U.nombre, COUNT(R.id) AS reservas_hechas
FROM usuarios U
LEFT JOIN usuario_reserva UR ON U.id = UR.id_usuario
LEFT JOIN reservas R ON UR.id_reserva = R.id
GROUP BY U.id;