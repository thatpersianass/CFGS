-- Procedimiento 1 --
DELIMITER //

CREATE PROCEDURE ObtenerEstadisticasEnviosCliente (
    IN p_DNI_cliente VARCHAR(20),
    OUT total_envios INT,
    OUT entregados INT,
    OUT pendientes INT,
    OUT cancelados INT
)
BEGIN
    DECLARE num INT;

    SELECT COUNT(*) INTO num
    FROM Envios
    WHERE DNI_cliente = p_DNI_cliente;

    IF num = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No existen envíos para el cliente especificado';
    ELSE	
        SELECT COUNT(*) INTO total_envios
        FROM Envios
        WHERE DNI_cliente = p_DNI_cliente;

        SELECT COUNT(*) INTO entregados
        FROM Envios
        WHERE DNI_cliente = p_DNI_cliente AND estado_envio = 'Entregado';

        SELECT COUNT(*) INTO pendientes
        FROM Envios
        WHERE DNI_cliente = p_DNI_cliente AND estado_envio = 'Pendiente';

        SELECT COUNT(*) INTO cancelados
        FROM Envios
        WHERE DNI_cliente = p_DNI_cliente AND estado_envio = 'Cancelado';
    END IF;
END //

DELIMITER ;


-- Procedimiento 2 --
DELIMITER //

CREATE PROCEDURE AsignarEnviosPendientesConductor (
    IN p_DNI_conductor VARCHAR(20)
)
BEGIN

    DECLARE v_id_envio INT;
    DECLARE fin_cursor BOOLEAN DEFAULT FALSE;

    DECLARE cursor_envios CURSOR FOR
        SELECT id_envio
        FROM Envios
        WHERE estado_envio = 'Pendiente' AND DNI_conductor IS NULL;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET fin_cursor = TRUE;

    OPEN cursor_envios;

    leer_envio: LOOP
        FETCH cursor_envios INTO v_id_envio;
        IF fin_cursor THEN
            LEAVE leer_envio;
        END IF;

        UPDATE Envios
        SET DNI_conductor = p_DNI_conductor
        WHERE id_envio = v_id_envio;
    END LOOP;

    CLOSE cursor_envios;
END //

DELIMITER ;

-- Procedimiento 3 --
DELIMITER //

CREATE PROCEDURE ResumenKilometrosPorConductor (
    IN  p_DNI_conductor   VARCHAR(20),
    OUT total_kilometros  INT
)
BEGIN
    DECLARE v_id_ruta    INT;
    DECLARE v_km         INT DEFAULT 0;
    DECLARE fin_cursor   BOOLEAN DEFAULT FALSE;

    DECLARE cursor_rutas CURSOR FOR
        SELECT E.id_ruta
        FROM Envios E
        WHERE E.DNI_conductor = p_DNI_conductor
          AND E.estado_envio   = 'Entregado';

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET fin_cursor = TRUE;

    SET total_kilometros = 0;

    OPEN cursor_rutas;
    recorrer_rutas: LOOP
        FETCH cursor_rutas INTO v_id_ruta;
        IF fin_cursor THEN
            LEAVE recorrer_rutas;
        END IF;

        SELECT kilometros INTO v_km
        FROM Rutas
        WHERE id_ruta = v_id_ruta;

        SET total_kilometros = total_kilometros + v_km;
    END LOOP;
    CLOSE cursor_rutas;
END //

DELIMITER ;