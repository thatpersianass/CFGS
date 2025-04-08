DELIMITER $$
CREATE TRIGGER alerta_stock_bajo
AFTER UPDATE ON Productos
FOR EACH ROW
BEGIN
    IF NEW.stock < 3 THEN
        INSERT INTO Historial_auditoria (id_venta, evento, fecha_evento)
        VALUES (NULL, CONCAT('¡Alerta! Stock bajo para el producto ID ', NEW.id_pro, ', stock actual: ', NEW.stock), NOW());
    END IF;
END $$
DELIMITER ;
