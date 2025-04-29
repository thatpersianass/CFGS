-- Funcion 1 --
DELIMITER $$
CREATE FUNCTION CantidadEnvios(
    p_dni_cliente VARCHAR(20),
    p_tipo_vehiculo VARCHAR(50)
)
RETURNS INT
DETERMINISTIC
READS SQL DATA
BEGIN
    DECLARE cantidad INT DEFAULT 0;
    SELECT COUNT(*)
    INTO cantidad
    FROM Envios AS E
    INNER JOIN Vehiculos AS V ON E.placa = V.placa
    WHERE E.DNI_cliente = p_dni_cliente
      AND V.tipo_vehiculo = p_tipo_vehiculo;
    RETURN cantidad;
END $$
DELIMITER ;

-- Funcion 2 --
DELIMITER $$
CREATE FUNCTION PromedioDistancia(
    p_dni_conductor VARCHAR(20)
)
RETURNS DECIMAL(10,2)
DETERMINISTIC
READS SQL DATA
BEGIN
    DECLARE promedio DECIMAL(10,2) DEFAULT 0;
    SELECT AVG(R.distancia_km) INTO promedio
    FROM Envios AS E
    INNER JOIN Rutas AS R ON E.id_ruta = R.id_ruta
    WHERE E.DNI_conductor = p_dni_conductor
      AND E.estado_envio = 'Entregado';
    RETURN IFNULL(promedio, 0);
END $$
DELIMITER ;
