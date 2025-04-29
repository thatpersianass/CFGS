-- TRIGGER 1 --
DELIMITER $$
CREATE TRIGGER comprobar_estado_vehiculo
BEFORE INSERT ON Envios
FOR EACH ROW
BEGIN
    DECLARE estado_actual ENUM('Disponible', 'En Ruta', 'En Mantenimiento');    
    SELECT estado INTO estado_actual
    FROM Vehiculos
    WHERE placa = NEW.placa;
    IF estado_actual IS NULL THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Error: El vehículo indicado no se encuentra registrado.';
    ELSEIF estado_actual != 'Disponible' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Error: El vehículo no se encuentra disponible para el envío.';
    END IF;
END $$
DELIMITER ;

-- TRIGGER 2 --
DELIMITER $$
CREATE TRIGGER modificar_estado_vehiculo
AFTER UPDATE ON Envios
FOR EACH ROW
BEGIN
    IF OLD.estado_envio != NEW.estado_envio THEN
        IF NEW.estado_envio = 'En tránsito' THEN
            UPDATE Vehiculos
            SET estado = 'En Ruta'
            WHERE placa = NEW.placa;
        ELSEIF NEW.estado_envio IN ('Entregado', 'Cancelado') THEN
            UPDATE Vehiculos
            SET estado = 'Disponible'
            WHERE placa = NEW.placa;
        END IF;
    END IF;
END $$
DELIMITER ;

-- TRIGGER 3 --
DELIMITER $$
CREATE TRIGGER registrar_auditoria_envios
AFTER UPDATE ON Envios
FOR EACH ROW
BEGIN
    IF OLD.estado_envio <> NEW.estado_envio THEN
        INSERT INTO AuditoriaEnvios (id_envio, estado_anterior, estado_nuevo, fecha_cambio)
        VALUES (NEW.id_envio, OLD.estado_envio, NEW.estado_envio, NOW());
    END IF;
END $$
DELIMITER ;